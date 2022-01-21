"""
ASGI config for TicTacToe project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from django.urls import path
from Game.consumers import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TicTacToe.settings')

# application = get_asgi_application()


ws_pattern=[
    path('ws/game/<room_code>',GameRoom.as_asgi())
]

application=ProtocolTypeRouter(
    {
        'websocket':AuthMiddlewareStack(URLRouter(
            ws_pattern
        ))
    }
)
