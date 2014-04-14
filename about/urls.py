from django.conf.urls import patterns, url

from about import views

urlpatterns = patterns('', 
  url(r'^$', views.index, name='aboutindex'), # ex: /about/
  url(r'^(?P<page_id>\d+)/$', views.detail, name='aboutdetail'), # ex: /about/2/
)
