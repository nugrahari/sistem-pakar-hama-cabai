from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
	path('api/login', views.obtain_auth_token, name='api_login_api'),
]