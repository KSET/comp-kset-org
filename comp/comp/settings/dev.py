from .base import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'compdb.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_TO_ADDRESS = 'test@test.com' 
