from .base import *


SECURE_HSTS_SECONDS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
