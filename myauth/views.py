from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from random import randint

from django.contrib.auth.models import User
from myauth.models import Two_factor

from twilio.rest import TwilioRestClient
from django.core.mail import send_mail
from django.conf import settings
from django.core.signing import Signer
import base64

def register(request):
	return render(request, 'myauth/register.html', {})

def register_submit(request):
	user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
	user.save()
	tf = Two_factor.objects.create(user=user, phone_token=generate_token(), email_token=generate_token(), phone_verified=False, email_verified=False, phone_number=request.POST['phone_number'])
	tf.save()
	send_token_sms(tf.phone_number, tf.phone_token)
	send_confirmation_mail(user.email, tf.email_token, user.username)
	return HttpResponse("Details submitted!")

def confirm_email(request):
	username = request.GET['username']
	signature = request.GET['signature']
	signer = Signer()
	#TODO: Try catch for unsign
	received_token = str(signer.unsign(signature))
	# TODO: Try catch for user fetch
	user = Two_factor.objects.get(user__username=username)
	if user.email_token == received_token:
		response = "thank you for confirming your email"
	else:
	 	response = "Invalid URL"
	return HttpResponse(response)

def signin(request):
	return render(request, 'myauth/signin.html', {})

def verify_user(request):
	response = "Username: %s Password: %s" % (request.POST['username'], request.POST['password'])
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		response = "success!"
		if user.is_active:
			user = Two_factor.objects.get(user__username=username)
			user.phone_token = generate_token()
			user.save()
			send_token_sms(user.phone_number, user.phone_token)
			context = {'username': username, 'phone_number': obfuscate(user.phone_number)}
			return render(request, 'myauth/sms.html', context)
		else:
			pass
	else:
		return render(request, 'myauth/signin.html', {'error_msg': "Incorrect username/password"})

def sms_verify(request):
	#return render(request, 'myauth/sms.html', {})
	response = request.POST['username']
	return HttpResponse(response)

def check_token(request):
	username = request.POST['username']
	token = request.POST['token']
	try:
		user = Two_factor.objects.get(user__username=username)
	except Exception:
		#redirect to signin page
		pass
	else:
		if user.phone_token == token:
			return HttpResponse("Log in successful!")
		else:
			#sign in again
			return HttpResponse("Bad Token!")

def obfuscate(phone_number):
	n = []
	for c in phone_number:
		if len(n) < 4:
			n.append(c)
		else:
			n.append('*')
	return ''.join(n)


def generate_token():
	return randint(1000, 9000)

def send_token_sms(phone_number, token):
	client = TwilioRestClient(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
	client.messages.create(
		to=phone_number, 
		from_="+12019891573", 
		body=token,  
	)

def send_confirmation_mail(email, token, username):
	to = email
	subject = "Email Confirmation"
	signer = Signer()
	signature = signer.sign(token)
	url = 'http://127.0.0.1:8000/myauth/confirmemail/?username=' + username + '&signature=' + signature
	content = "Hi %s!,\n\nThank you for registering on our site.\n\nClick on the url below to confirm your email:\n\n%s\n\nThanks!" % (username, url)
	send_mail(subject, content, settings.EMAIL_HOST_USER, [to], fail_silently=False)