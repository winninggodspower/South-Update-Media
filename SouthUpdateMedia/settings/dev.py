from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ALLOWED_HOSTS = ["southupdatemedia.com", "127.0.0.1", 'localhost', "*"]

try:
    from .local import *
except ImportError:
    pass
