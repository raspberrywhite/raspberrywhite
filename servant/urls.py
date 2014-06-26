from django.conf.urls import patterns, include, url
from server.views import login, register, playlist, songrequest
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'servant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^playlist/$',  playlist),
    (r'^request/$',  songrequest),
    (r'^accounts/login/$',  login),
    (r'^accounts/register/$',  register),
)