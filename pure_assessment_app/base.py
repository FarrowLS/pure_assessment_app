"""
Django settings for pure_assessment_app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/

settings/base.py
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# ImproperlyConfigured imported to handle SECRET_KEY exceptions
# See page 46 in Two Scoops of Django 1.6 for details
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    try: 
        return os.environ[var_name]
    except KeyError:
        error_msq = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY is handled by an environmental variable for security purposes
SECRET_KEY = os.environ["SECRET_KEY"]


# SECURITY WARNING: don't run with debug turned on in production!
# Settings move to environment setting files
# DEBUG = True
# TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'admin_honeypot',
    # For django-allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount', 
    # Start custom apps
    'about',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pure_assessment_app.urls'

WSGI_APPLICATION = 'pure_assessment_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# STATIC_URL = '/static/'

# Added to allow template files to be served from multiple directories
# http://stackoverflow.com/questions/11768143/heroku-cant-find-django-templates
PROJECT_DIR = os.path.dirname(__file__) # this is not a standard Django setting.
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"),
    # here you can add another templates directory if you wish.
    os.path.join(PROJECT_DIR, "templates", "allauth", "templates"),
)

# Static asset configuration
# import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Settings for django-allauth (from https://github.com/pennersr/django-allauth)
TEMPLATE_CONTEXT_PROCESSORS = (
    # Required by allauth template tags
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth", # added on guidance from http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

# Continued settings for django-allauth
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

# auth and allauth settings for django-allauth from http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/
LOGIN_REDIRECT_URL = '/'
# SOCIALACCOUNT_QUERY_EMAIL = True
# SOCIALACCOUNT_PROVIDERS = {}
SITE_ID = 1 
