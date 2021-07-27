from django.db import models
from django.dispatch import receiver
from app_cabai.asgi.consumers import WSConsumer
from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.
class Notification(models.Model):
	title = models.CharField(max_length=100)
	subtitle = models.TextField(blank=True, null=True)
	def __str__(self):
		return "{}. {}".format(self.id, self.title)

from django.conf import settings
from rest_framework.authtoken.models import Token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import sys

channel_layer = get_channel_layer()

@receiver(models.signals.post_save, sender=Notification)
def send_notifications(sender, instance, *args, **kwargs):
	message = {        
		'title': instance.title,
		'subtitle': instance.subtitle,
		'is_readed': False,
	}
	print(message)
	message = json.dumps(message)
	print(message)
	async_to_sync(channel_layer.group_send)(
		'allUser',
		{
			'type': 'send_message',
			'text': message
		}
	)

