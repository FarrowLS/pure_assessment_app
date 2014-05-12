# settings/development.py

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR_PATCH_SETTINGS = False

INSTALLED_APPS += (
    'debug_toolbar',
    "sslserver",
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pure_assessment_app',
        'USER': 'peterfarrow',
        'PASSWORD': os.environ["DEV_DATABASE_PASSWORD"],
        'HOST': '',
        'PORT': '',
    }
}
