from django.urls import path
from rest_framework.authtoken import views
from app_user.api.views import RegisterAPI

urlpatterns = [
	path('api/login', views.obtain_auth_token, name='api_login_api'),
	path('api/register', RegisterAPI.as_view(), name='api_register'),
]