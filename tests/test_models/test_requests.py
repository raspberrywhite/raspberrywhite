import django
from django.contrib.auth.models import User as AuthUser
from mock import patch
from server.models import Request, Song, Player

class RequestModelTestCase(django.test.TestCase):

    @patch('server.models.hotstuff.users.time')
    def setUp(self, mock_time):
        self.user = AuthUser.objects.create_user(username='barry', email='barry@white.com',
            password='myeverything')
        self.player = Player.objects.create(user=self.user)
        self.song = Song.songs.create(title='Title 1', artist='Artist 1', path='Path 1', last_time_play=3600)
        mock_time.time.return_value = 2000
        Request.requests.create(user=self.player, song=self.song)
        mock_time.time.return_value = 2100
        Request.requests.create(user=self.player, song=self.song)
        mock_time.time.return_value = 2200
        Request.requests.create(user=self.player, song=self.song)

    def test_get_all_requests_ordered_by_priority_by_default(self):
        requests = Request.requests.all()
        self.assertTrue(requests[0].priority <= requests[1].priority)
        self.assertTrue(requests[1].priority <= requests[2].priority)

    def test_get_request_with_max_priority(self):
        request = Request.requests.get_max()
        self.assertEqual(request.priority, 100)

    @patch('server.models.hotstuff.users.time')
    def test_save_priority_automatically(self, mock_time):
        mock_time.time.return_value = 2900
        request = Request.requests.create(user=self.player, song=self.song)
        self.assertEqual(request.priority, 700)

