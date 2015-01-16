import django
from django.contrib.auth.models import User as AuthUser
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.utils.html import escape

import json
from mock import patch
from popmuzik import Popmuzik
from requests.exceptions import ConnectionError

class MockResponse():
    def __init__(self, status_code, text=''):
        self.status_code = status_code
        self.text = text

    def json(self):
        return json.loads(self.text)

class TestPopomuzik(django.test.TestCase):

    def setUp(self):
        self.player = Popmuzik()

    def tearDown(self):
        pass

    @patch('popmuzik.player.Mp3Player.play')
    @patch('popmuzik.requests')
    def test_player_call_play_on_next_request_ok(self, mock_requests, mock_player):
        mock_requests.get.return_value = MockResponse(200, '{"path" : "/hello/song"}')
        self.player.requestSong()
        mock_player.assert_called_with('/hello/song')

    @patch('popmuzik.Popmuzik.onFetchingFail')
    @patch('popmuzik.requests')
    def test_player_call_fail_cb_on_next_request_ko(self, mock_requests, mock_fetching_fail_cb):
        mock_requests.get.return_value = MockResponse(404)
        self.player.requestSong()
        mock_fetching_fail_cb.assert_called()

    @patch('popmuzik.Popmuzik.onFetchingFail')
    @patch('popmuzik.requests')
    def test_player_call_fail_cb_on_connection_error(self, mock_requests, mock_fetching_fail_cb):
        mock_requests.get.side_effect = ConnectionError('Connection error!')
        self.player.requestSong()
        mock_fetching_fail_cb.assert_called()

