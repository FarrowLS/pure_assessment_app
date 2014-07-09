from django.conf.urls import patterns, url

# from itembank import views

urlpatterns = patterns('itembank.views',
    url(r'^apiv1/items/$', 'item_list'),
    url(r'^apiv1/items/(?P<pk>[0-9]+)/$', 'item_detail'),
)