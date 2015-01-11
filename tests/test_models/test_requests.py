import django
from django.contrib.auth.models import User as AuthUser
from server.models import Request, Song, Player

class RequestModelTestCase(django.test.TestCase):

    def setUp(self):
        user = AuthUser.objects.create_user(username='barry', email='barry@white.com',
            password='myeverything')
        player = Player.objects.create(user=user)
        song = Song.songs.create(title='Title 1', artist='Artist 1', path='Path 1', last_time_play=3600)
        Request.requests.create(user=player, song=song, priority=100)
        Request.requests.create(user=player, song=song, priority=300)
        Request.requests.create(user=player, song=song, priority=200)

    def test_get_all_requests_ordered_by_priority_by_default(self):
        requests = Request.requests.all()
        self.assertTrue(requests[0].priority < requests[1].priority)
        self.assertTrue(requests[1].priority < requests[2].priority)

    def test_get_request_with_max_priority(self):
        request = Request.requests.get_max()
        self.assertEqual(request.priority, 100)

    def test_save_priority_automatically(self):
        pass