from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from random import randint

from django.contrib.auth.models import User
from myauth.models import Two_factor
from django.core.mail import send_mail
from django.conf import settings
from django.core.signing import Signer

from django_otp.decorators import otp_required

def register(request):
	return render(request, 'myauth/register.html', {})

def register_submit(request):
	username = request.POST['username']
	password = request.POST['password']
	user = User.objects.create_user(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=username, email=request.POST['email'], password=password)
	user.save()
	tf = Two_factor.objects.create(user=user, email_token=generate_token(), email_verified=False)
	tf.save()
	send_confirmation_mail(user.email, tf.email_token, user.username)
	auth_user = authenticate(username=request.POST['username'], password=request.POST['password'])
	login(request, auth_user)
	return HttpResponseRedirect(reverse('two_factor:setup'))


def confirm_email(request):
	username = request.GET['username']
	signature = request.GET['signature']
	signer = Signer()
	try:
		received_token = str(signer.unsign(signature))
	except Exception, e:
		response = "Invalid URL"
	else:
		try:
			user = Two_factor.objects.get(user__username=username)
		except Exception, e:
			response = "Invalid URL"
		else:
			if user.email_token == received_token:
				user.email_verified = True
				user.save()
				response = "thank you for confirming your email"
			else:
			 	response = "Invalid URL"
	return HttpResponse(response)

def logoutview(request):
	logout(request)
	return HttpResponseRedirect(reverse('myauth:signin'))


def generate_token():
	return randint(1000, 9000)


def send_confirmation_mail(email, token, username):
	to = email
	subject = "Verify your email address"
	signer = Signer()
	signature = signer.sign(token)
	url = 'http://127.0.0.1:8000/myauth/confirmemail/?username=' + username + '&signature=' + signature
	content = "Hi %s!,\n\nThank you for registering on our site.\n\nClick on the url below to confirm your email:\n\n%s\n\nThanks!" % (username, url)
	send_mail(subject, content, settings.EMAIL_HOST_USER, [to], fail_silently=False)


@otp_required
def restricted(request):
	return HttpResponse("Successful two_factor login")
	# if request.user.is_verified():
	# 	return HttpResponse("Login successful")
	# else:
	# 	return HttpResponse("You are not verified!")

