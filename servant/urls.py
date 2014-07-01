from django.conf import settings
from django.conf.urls import patterns, include, url
from server.views import login, register, get_current_playlist, playlist
from server.views import songrequest, search_songs, get_next_song, SSE
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'servant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sse/(?P<channel>\w+)/$', SSE.as_view(redis_channel="foo"), name='sse'),
    (r'^playlist/$', playlist),
    (r'^playlist/current$', get_current_playlist),
    (r'^request/$', songrequest),
    (r'^accounts/login/$', login),
    (r'^accounts/register/$', register),
    (r'^songs/$', search_songs),
    (r'^songs/next/$', get_next_song)
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)