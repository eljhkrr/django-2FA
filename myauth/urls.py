from django.conf.urls import url

from myauth import views

urlpatterns = [
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^register/$', views.register, name='register'),
	url(r'^verify_user/$', views.verify_user, name='verify_user'),
	url(r'sms/$', views.sms_verify, name="verify_sms"),
	url(r'checktoken/$', views.check_token, name="check_token"),
]