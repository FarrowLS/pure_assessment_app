# settings/development.py

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

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


# Static asset configuration - Moved to base.py settings file
# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/static/'
# 
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# ) 
