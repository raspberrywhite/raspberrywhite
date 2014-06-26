from django.conf.urls import patterns, include, url
from server.views import login, register
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'servant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$',  login),
    (r'^accounts/register/$',  register),
)