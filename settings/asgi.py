"""
ASGI config for blog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
import modulefinder
import os

from django.core.asgi import get_asgi_application

from settings.environment.settings import *

application = get_asgi_application()
