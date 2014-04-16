from django.conf.urls import patterns, include, url

from django.http import HttpResponseRedirect

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pure_assessment_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # For redirecting root url
    (r'^$', lambda r : HttpResponseRedirect('about/')),
)

