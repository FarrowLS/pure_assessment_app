from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from item import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.index), name='itemindex'), # ex: /items/
)