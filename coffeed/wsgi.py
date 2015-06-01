"""
WSGI config for coffeed project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

# Next line hashed out by keith 010615 (Project 1 Lesson 8)
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coffeed.settings")

application = Cling(get_wsgi_application())
