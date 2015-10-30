from django.core.signing import Signer
from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_mail(email, token, username):
	to = email
	subject = "Verify your email address"
	signer = Signer()
	signature = signer.sign(token)
	url = 'http://127.0.0.1:8000/myauth/confirmemail/?username=' + username + '&signature=' + signature
	content = "Hi %s!,\n\nThank you for registering on our site.\n\nClick on the url below to confirm your email:\n\n%s\n\nThanks!" % (username, url)
	send_mail(subject, content, settings.EMAIL_HOST_USER, [to], fail_silently=False)
