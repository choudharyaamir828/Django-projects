import json
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'chatbot'
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        
        # Send welcome message
        await self.send(text_data=json.dumps({
            'type': 'connection',
            'message': 'Connected to chatbot!'
        }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')


        response = await self.generate_ai_response(message)

        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'response': response
            }
        )

    async def chat_message(self, event):
        message = event['message']
        response = event['response']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'message',
            'user_message': message,
            'bot_response': response
        }))

    async def generate_ai_response(self, user_message):
        """Simulate AI response generation"""
        await asyncio.sleep(1)
        
        responses = {
            'hello': 'Hello! How can I help you today?',
            'hi': 'Hi there! What can I do for you?',
            'how are you': 'I\'m doing great! Thanks for asking.',
            'bye': 'Goodbye! Have a great day!',
            'what is your name': 'I am BOL7 ChatBot, your virtual assistant.'
        }
        
        user_message_lower = user_message.lower().strip()
        
        if user_message_lower in responses:
            return responses[user_message_lower]
        else:
            return f"You said: {user_message}. This is where AI processing happens!"