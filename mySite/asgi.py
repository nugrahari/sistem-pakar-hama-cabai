"""
ASGI config for mySite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack

from app_cabai.asgi.routing import wsurlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mySite.settings')

application = ProtocolTypeRouter({

		'http' :get_asgi_application(),
		'websocket' : AuthMiddlewareStack(URLRouter(wsurlpatterns))
	}

)
# application = get_asgi_application()
