from django.db.models.signals import post_save
from django.dispatch import receiver
from myauth.models import Two_factor, Question
from myauth.views import send_confirmation_mail

@receiver(post_save, sender=Two_factor)
def tf_post_save(sender, **kwargs):
	instance = kwargs['instance']
	print "User email: ", instance.user.email
	send_confirmation_mail(instance.user.email, instance.email_token, "Baaaaaah!!")