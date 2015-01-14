from django.contrib.auth.models import User as AuthUser
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.utils.html import escape

from server.models import Player, Song, Request

class SongRequestTest(TestCase):

    def test_saving_a_new_song_request(self):
        self.user = AuthUser.objects.create_user(username='barry', email='barry@white.com',
            password='myeverything')
        self.song = Song.songs.create(pk=43, title='Title 1',
            artist='Artist 1', path='Path 1', last_time_play=0)
        self.client.login(username='barry', password='myeverything')
        self.client.post(
            '/request/',
            data={'id_song': 43}
        )
        self.assertEqual(Request.requests.count(), 1)
        new_request = Request.requests.first()
        self.assertEqual(new_request.song.pk, 43)
