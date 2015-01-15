from django.contrib.auth.models import User as AuthUser
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.utils.html import escape

import json
from mock import patch
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

    @patch('server.models.time')
    def test_get_next_request(self, mock_time):
        self.user = AuthUser.objects.create_user(username='barry', email='barry@white.com',
            password='myeverything')
        self.player = Player.objects.create(user=self.user)
        self.song = Song.songs.create(pk=43, title='Title 1',
            artist='Artist 1', path='Path 1', last_time_play=0)

        mock_time.time.return_value = 2000
        Request.requests.create(user=self.player, song=self.song)
        mock_time.time.return_value = 2100
        Request.requests.create(user=self.player, song=self.song)

        self.client.get(
            '/songs/next/'
        )
        self.assertEqual(Request.requests.count(), 2)

        self.client.get(
            '/songs/next/'
        )
        self.assertEqual(Request.requests.count(), 1)

        self.client.get(
            '/songs/next/'
        )
        self.assertEqual(Request.requests.count(), 0)


class PlaylistTest(TestCase):

    def setUp(self):
        self.user = AuthUser.objects.create_user(username='barry', email='barry@white.com',
            password='myeverything')
        self.player = Player.objects.create(user=self.user)

        self.song1 = Song.songs.create(title='Title 1',
            artist='Artist 1', path='Path 1', last_time_play=0)

        self.song2 = Song.songs.create(title='Title 2',
            artist='Artist 2', path='Path 2', last_time_play=0)

        Request.requests.create(user=self.player, song=self.song1)
        Request.requests.create(user=self.player, song=self.song2)

        self.client.login(username='barry', password='myeverything')

    def test_playlist_read(self):
        resp = self.client.get(
            '/playlist/current'
        )
        self.assertEqual(len(json.loads(resp.content)), 2)

    def test_playlist_after_new_request(self):
        resp = self.client.get(
            '/playlist/current'
        )

        playlist = json.loads(resp.content)
        self.assertFalse(playlist[0]['now_play'])

        self.assertEqual(len(playlist), 2)
        self.client.get(
            '/songs/next/'
        )

        resp = self.client.get(
            '/playlist/current'
        )
        playlist = json.loads(resp.content)
        self.assertTrue(playlist[0]['now_play'])

        self.client.get(
            '/songs/next/'
        )
        resp = self.client.get(
            '/playlist/current'
        )
        playlist = json.loads(resp.content)
        self.assertEqual(len(playlist), 1)
        self.assertTrue(playlist[0]['now_play'])

    def test_playlist_empty(self):
        for i in range(3):
            self.client.get(
                '/songs/next/'
            )
        resp = self.client.get(
            '/playlist/current'
        )
        playlist = json.loads(resp.content)
        self.assertEqual(len(playlist), 0)
