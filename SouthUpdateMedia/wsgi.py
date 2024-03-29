"""
WSGI config for SouthUpdateMedia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"SouthUpdateMedia.settings.{os.getenv('ENVIRONMENT')}")

application = get_wsgi_application()
