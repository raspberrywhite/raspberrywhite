import django
from mock import patch
from server.models import Song

class SongModelTestCase(django.test.TestCase):

    def setUp(self):
        Song.songs.create(title='Title 1', artist='Artist 1', path='Path 1', last_time_play=3600)
        Song.songs.create(title='Title 2', artist='Artist 2', path='Path 2', last_time_play=0)
        Song.songs.create(title='Title 3', artist='Artist 3', path='Path 3', last_time_play=0)
        Song.songs.create(title='Title 4', artist='Artist 4', path='Path 4', last_time_play=0)

    def test_filter_song_by_artist_title(self):
        songs = Song.songs.query('Title')
        self.assertEqual(len(songs), 4)
        songs = Song.songs.query('Artist 1')
        self.assertEqual(len(songs), 1)

    def test_filter_song_by_artist_title_no_result(self):
        songs = Song.songs.query('WrongArtist 1')
        self.assertEqual(len(songs), 0)

    def test_get_all_songs_with_empty_query(self):
        songs = Song.songs.query('')
        self.assertEqual(len(songs), 4)

    @patch('server.models.time')
    def test_can_play(self, mock_time):
        mock_time.time.return_value = 7200
        song = Song.songs.get(title='Title 1')
        self.assertTrue(song.can_play())

    @patch('server.models.time')
    def test_cannot_play(self, mock_time):
        mock_time.time.return_value = 1
        song = Song.songs.get(title='Title 1')
        self.assertFalse(song.can_play())