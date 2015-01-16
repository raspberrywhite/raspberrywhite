import django
import player
from player import Mp3Player, PlayerListener
import time

class TestPlayer(django.test.TestCase):

    def setUp(self):
        self.filename = 'player/tests/assets/test.mp3'
        self.filename_bad = 'player/tests/assets/raspiwhite.png'
        self.player = Mp3Player()

    def tearDown(self):
        pass

    def test_play_song(self):
        pass

    def test_play_commands(self):
        pass

    def test_bad_file(self):
        pass

    def test_bad_path(self):
        pass
