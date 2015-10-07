from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from myauth.models import Two_factor

class Two_factorInline(admin.StackedInline):
	model = Two_factor
	can_delete = False
	verbose_name_plural = 'two_factor'

class UserAdmin(UserAdmin):
	inlines = (Two_factorInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)