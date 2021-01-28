import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class PostConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add('entries', self.channel_name)
        print(f"Added {self.channel_name} channel to entries")

    async def disconnect(self, code):
        await self.channel_layer.group_discard('entries', self.channel_name)
        print(f"Added {self.channel_name} channel to entries")
        # await super().disconnect(code)

    async def blog_entries(self, event):
        await self.send_json(event)
        print(event)