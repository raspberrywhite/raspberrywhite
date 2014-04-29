from hotstuff import calc_priority
from hotstuff import calc_priority_now
from mock import Mock

class TestUsers():

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calc_priority(self):
        assert calc_priority(1000000, 3000000) == 2000000

    def test_calc_priority_now(self):
        import time
        time_fun = time.time
        time.time = Mock(return_value=2000)
        assert calc_priority_now(1000000) == 1000000
        time.time = time_fun