from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from myauth.models import Two_factor
from random import randint

def register(request):
	return HttpResponse("Register!")

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
			user.phone_token = randint(1000, 9000)
			#send token over sms
			user.save()
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


