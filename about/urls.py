from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from about import views

urlpatterns = patterns('', 
  url(r'^$', views.index, name='aboutindex'), # ex: /about/
  url(r'^(?P<pk>\d+)/$', login_required(views.DetailView.as_view()), name='aboutdetail'), # ex: /about/2/ with access control
  # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='aboutdetail'), # ex: /about/2/ without access control
)
