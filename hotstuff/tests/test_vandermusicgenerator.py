import django
from hotstuff.vandermusicgenerator import generate
from mock import patch
from server.models import Request, Song, Player

class TestVanDerMusicGenerator(django.test.TestCase):

    def setUp(self):
        pass

    def test_insert_new_songs_after_generate(self):
        generate('hotstuff/tests/assets/')
        self.assertEquals(len(Song.songs.all()), 1)

    def test_do_not_insert_the_same_song(self):
        generate('hotstuff/tests/assets/')
        self.assertEquals(len(Song.songs.all()), 1)
        generate('hotstuff/tests/assets/')
        self.assertEquals(len(Song.songs.all()), 1)