from django.conf.urls import url

from myauth import views

urlpatterns = [
	url(r'^register/$', views.register, name='register'),
	url(r'registersubmit/$', views.register_submit, name="register_submit"),
	url(r'confirmemail/$', views.confirm_email, name="confirm_email"),
	url(r'restricted/$', views.restricted, name="restricted"),
	url(r'logout/$', views.logoutview, name="logout"),
]