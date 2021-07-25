import json
import time
from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer

class WSConsumer(AsyncWebsocketConsumer):
	async def connect(self):

		await self.channel_layer.group_add(
	        'allUser',
	        self.channel_name
	    )
		await self.accept()
		
		for i in range(1):
			message = {        
				'title': f'Selamat Datang Kembali',
				'subtitle': f'Ini adalah aplikasi untuk diagnosa penyakit cabai',
				'is_readed': False,
			}
			# await print('sending web socket')
			await self.send(json.dumps(message))
			await sleep(1)

	async def disconnect(self):
		await self.channel_layer.group_discard(
	        'allUser',
	        self.channel_name
	    )

	async def send_message(self, event):
	    message = event['text']
	    print(event)
	    await self.send(message)
	
	# def send(self):
	# 	for i in range(100000):
	# 		message ={
	# 			'data'	: i,
	# 		}
	# 		self.send(json.dumps(message))
	# 		time.sleep(1)
