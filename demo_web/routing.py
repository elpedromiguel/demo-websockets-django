from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

# from apps.services.consumers import  ServiceConsumer

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    # 'websocket': URLRouter([
    #     path('services/', ServiceConsumer.as_asgi()),
    # ]),
})