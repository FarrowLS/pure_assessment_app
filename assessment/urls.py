from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from assessment import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.index), name='assessmentindex'), # ex: /assessment/
    url(r'^item/$', login_required(views.item), name='assessmentitem'), # ex: /assessment/item
    url(r'^response/$', login_required(views.response), name='assessmentresponse'), # ex: /assessment/response
) 
