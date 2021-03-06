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

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY is handled by an environmental variable for security purposes
SECRET_KEY = os.environ["SECRET_KEY"]


# Debuging handled in settings/development.py

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
    'djangosecure',
    'admin_honeypot',
    # For django-allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount', 
    # For djangorestframework
    'rest_framework',
    # Start custom apps
    'about',
    'assessment', 
    'itembank',
)

MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pure_assessment_app.urls'

WSGI_APPLICATION = 'pure_assessment_app.wsgi.application'

# django-secure settings
SECURE_SSL_REDIRECT = True    
SECURE_HSTS_SECONDS = 3600
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# Related security settings
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}

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

# Template and static file section
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Added to allow template files to be served from multiple directories
# http://stackoverflow.com/questions/11768143/heroku-cant-find-django-templates
PROJECT_DIR = os.path.dirname(__file__) 
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
    # For messages framework
    "django.contrib.messages.context_processors.messages",
    # Required by allauth template tags
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth", # added on guidance from http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

# Continued settings for django-allauth
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

LOGIN_URL = '/accounts/login/'

# auth and allauth settings for django-allauth from http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/
# LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/assessments/'
# SOCIALACCOUNT_QUERY_EMAIL = True
# SOCIALACCOUNT_PROVIDERS = {}
SITE_ID = 1 
