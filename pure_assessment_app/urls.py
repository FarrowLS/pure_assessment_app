from django.conf.urls import patterns, include, url
from django.conf import settings
# from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pure_assessment_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # Core/contrib paths
    # allauth paths
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include('admin_honeypot.urls')),
    url(r'^notanormaladminpath/', include(admin.site.urls)),
    # My paths
    # url(r'^logout/', include('')),
    url(r'^about/', include('about.urls')), # about
    url(r'^assessments/', include('assessment.urls')),  # assessments
    # NOT CURRENTLY IN USE # url(r'^items/', include('item.urls')),  # items
    # For redirecting root url
    (r'^$', lambda r : HttpResponseRedirect('about/')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

