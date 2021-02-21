'''
Local development settings with postgresql local database

'''
from pathlib import Path
from ._base import *
import os


DEBUG = True

ALLOWED_HOSTS = ['*',]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dotenv',
    'apps.API',
    'apps.accounts',
    'apps.links',
    'apps.comments',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = Path(BASE_DIR / 'static')
<<<<<<< HEAD

=======
>>>>>>> 5195fb03ff926e54c15f3ecf2663bae7843745ff

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
