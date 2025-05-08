import json
from channels.generic.websocket import WebsocketConsumer


import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
class NotifyConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({
            'message': 'Connection Established'
        }))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'notify_message',
                'message': message
            }
        )

    def notify_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'Notification',
            'message': message
        }))

    