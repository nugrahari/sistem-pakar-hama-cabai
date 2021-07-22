from django.urls import path

from .consumers import WSConsumer

wsurlpatterns = [
  path('ws/some_url', WSConsumer.as_asgi())
]