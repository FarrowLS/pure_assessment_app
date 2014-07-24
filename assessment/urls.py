from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from assessment import views

urlpatterns = patterns('',
    url(r'^$', login_required(views.index), name='assessmentindex'), # ex: /assessments/
    url(r'^(?P<testeeassessment_id>\d+)/$', login_required(views.item), name='assessmentitem'), # ex: /assessments/123
    url(r'^(?P<testeeassessment_id>\d+)/feedback/$', login_required(views.feedback), name='assessmentfeedback'), # ex: /assessments/123/feedback
) 
