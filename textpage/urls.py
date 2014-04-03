from django.conf.urls import patterns, url

from textpage import views

urlpatterns = patterns('', 
  url(r'^$', views.index, name='index')
)
