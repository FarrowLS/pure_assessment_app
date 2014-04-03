"""
WSGI config for pure_assessment_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pure_assessment_app.settings")

# Standard Django settings for serving static files not currently in use
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()

# Settings from Heroku for serving static files
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
