from django.conf.urls import url

from myauth import views

urlpatterns = [
	url(r'^signin/$', views.signin, name='signin'),
	url(r'^register/$', views.register, name='register'),
	url(r'^verify_user/$', views.verify_user, name='verify_user'),
	url(r'sms/$', views.sms_verify, name="verify_sms"),
	url(r'checktoken/$', views.check_token, name="check_token"),
	url(r'registersubmit/$', views.register_submit, name="register_submit"),
	url(r'confirmemail/$', views.confirm_email, name="confirm_email"),
	url(r'content/$', views.content, name="content"),
]