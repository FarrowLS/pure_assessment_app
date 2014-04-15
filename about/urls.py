from django.conf.urls import patterns, url

from about import views

urlpatterns = patterns('', 
  url(r'^$', views.index, name='aboutindex'), # ex: /about/
  # Old FBV for detail page
  # url(r'^(?P<page_id>\d+)/$', views.detail, name='aboutdetail'), # ex: /about/2/
  url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='aboutdetail'), # ex: /about/2/ 
)
