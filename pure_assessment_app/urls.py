from django.conf.urls import patterns, include, url

from django.http import HttpResponseRedirect

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pure_assessment_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # Core/contrib paths
    (r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include('admin_honeypot.urls')),
    url(r'^notanormaladminpath/', include(admin.site.urls)),
    # My paths
    # url(r'^logout/', include('')),
    url(r'^about/', include('about.urls')),
    # For redirecting root url
    (r'^$', lambda r : HttpResponseRedirect('about/')),
)

