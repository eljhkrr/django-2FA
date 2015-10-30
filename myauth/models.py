from django.db import models
from django.contrib.auth.models import User

class Two_factor(models.Model):
	user = models.OneToOneField(User)
	email_token = models.CharField(max_length=100)
	email_verified = models.BooleanField()
