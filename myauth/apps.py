from django.apps import AppConfig

class MyauthConfig(AppConfig):
	name = "myauth"
	varbose_name = "MyAuth App"

	def ready(self):
		import myauth.signals
