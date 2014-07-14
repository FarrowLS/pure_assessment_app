from django.conf.urls import patterns, url

# from itembank import views

urlpatterns = patterns('itembank.views',

    # API paths for Itembank class
    url(r'^apiv1/itembanks/$', 'itembank_list', name='apiitembanklist'),
    url(r'^apiv1/itembanks/(?P<pk>[0-9]+)/$', 'itembank_detail', name='apiitembankdetail'),

    # API paths for Item class
    url(r'^apiv1/items/$', 'item_list'),
    url(r'^apiv1/items/(?P<pk>[0-9]+)/$', 'item_detail'),

)