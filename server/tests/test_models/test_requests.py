import django
from django.contrib.auth.models import User as AuthUser
from django.core.exceptions import ObjectDoesNotExist
from mock import patch
from server.models import Request, Song, Player

class RequestModelTestCase(django.test.TestCase):

    @patch('server.models.time')
    def setUp(self, mock_time):
        self.user = AuthUser.objects.create_user(username='barry', email='barry@white.com',
            password='myeverything')
        self.player = Player.objects.create(user=self.user)
        self.song = Song.songs.create(title='Title 1', artist='Artist 1', last_time_play=3600)
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
        self.assertEqual(request.priority, 0)

    @patch('server.models.time')
    def test_save_priority_automatically(self, mock_time):
        mock_time.time.return_value = 2900
        request = Request.requests.create(user=self.player, song=self.song)
        self.assertEqual(request.priority, 6300)

    @patch('server.models.time')
    def test_request_priority_boundaries(self, mock_time):
        mock_time.time.return_value = 9223372036854775807
        request = Request.requests.create(user=self.player, song=self.song)
        self.assertEqual(request.priority, 0)
        self.assertEqual(request.user.last_time_req, 0)

    def test_request_next(self):
        request = Request.requests.next()
        self.assertEqual(request.priority, 0)
        requests = Request.requests.all()
        self.assertEqual(len(requests), 3)

        request = Request.requests.next()
        self.assertEqual(request.priority, 2000)
        requests = Request.requests.all()
        self.assertEqual(len(requests), 2)

    def test_request_next_with_no_elements(self):
        Request.requests.next()
        Request.requests.next()
        Request.requests.next()
        self.assertRaises(ObjectDoesNotExist, Request.requests.next)

