# settings/development.py

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR_PATCH_SETTINGS = False
SOUTH_TESTS_MIGRATE = False

INSTALLED_APPS += (
    'debug_toolbar',
    "sslserver",
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

# Local dev setting to make HTTPS work. See the following sites for details:
# http://django-secure.readthedocs.org/en/v0.1.2/middleware.html#detecting-proxied-ssl
# https://docs.djangoproject.com/en/1.6/ref/settings/#std:setting-SECURE_PROXY_SSL_HEADER
SECURE_PROXY_SSL_HEADER = ('HTTP_HOST', 'localhost:8000')

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
