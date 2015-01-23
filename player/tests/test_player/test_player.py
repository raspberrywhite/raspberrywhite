import django
from mock import patch, MagicMock
import player
from player import Mp3Player, PlayerListener
import time

class TestPlayer(django.test.TestCase):

    def setUp(self):
        self.filename = 'player/tests/assets/test.mp3'
        self.bad_filename = 'player/tests/assets/raspiwhite.png'
        self.not_present_filename = 'player/tests/assets/testfake.mp3'
        self.player = Mp3Player()

    def tearDown(self):
        pass

    @patch('player.mp3player.AutoDetectThread')
    @patch('player.mp3player.subprocess.Popen')
    def test_play_song(self, mock_popen, mock_autodetectthread):
        self.player.play(self.filename)
        self.assertTrue(mock_autodetectthread.called)

    @patch('player.mp3player.AutoDetectThread')
    @patch('player.mp3player.subprocess.Popen')
    def test_play_song_not_present_file(self, mock_popen, mock_autodetectthread):
        self.player.play(self.not_present_filename)
        self.assertFalse(mock_autodetectthread.called)

    @patch('player.mp3player.AutoDetectThread')
    @patch('player.mp3player.subprocess.Popen')
    def test_on_event_call_listeners(self, mock_popen, mock_autodetectthread):
        mock_listener = MagicMock()
        self.player.attachListener(mock_listener)
        self.player.play(self.filename)
        mock_listener.onPlay.assert_called_once_with(self.filename)
        self.player.pause()
        mock_listener.onPause.assert_called_once_with()
        self.player.resume()
        mock_listener.onPause.assert_called_once_with()
        self.player.stop()
        mock_listener.onStop.assert_called_once_with()
        self.player.shutdown()
        mock_listener.onShutdown.assert_called_once_with()
