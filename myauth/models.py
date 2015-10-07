from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Two_factor(models.Model):
	user = models.OneToOneField(User)
	phone_number = models.CharField(max_length=20)
	phone_token = models.CharField(max_length=6)
	phone_verified = models.BooleanField()
	email_token = models.CharField(max_length=100)
	email_verified = models.BooleanField()
