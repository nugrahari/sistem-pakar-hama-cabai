from django.db import models
from django.dispatch import receiver
from app_cabai.asgi.consumers import WSConsumer
# Create your models here.
class Notification(models.Model):
	title = models.CharField(max_length=100)
	subtitle = models.TextField(blank=True, null=True)
	def __str__(self):
		return "{}. {}".format(self.id, self.title)


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import sys

# def send_message(event):
#     '''
#     Call back function to send message to the browser
#     '''
#     message = event['text']
#     channel_layer = channels.layers.get_channel_layer()
#     # Send message to WebSocket
#     async_to_sync(channel_layer.send)(text_data=json.dumps(
#         message
#     ))


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

