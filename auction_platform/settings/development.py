from .base import *
from datetime import timedelta

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# CORS settings for development
CORS_ALLOW_ALL_ORIGINS = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}