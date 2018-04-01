from api import api
import unittest


class TestGetTime(unittest.TestCase):
    def test_get_time_valid(self):
        result = api.get_time("2.5")
        self.assertEqual(result, {'hour': 2, 'minutes': 30})

    def test_get_time_empty(self):
        result = api.get_time()
        self.assertEqual(result, None)

    def test_get_time_none(self):
        result = api.get_time(None)
        self.assertEqual(result, None)

    def test_get_time_invalid_time(self):
        result = api.get_time("-50.0")
        self.assertEqual(result, None)

    def test_get_time_invalid_time2(self):
        # testing 110 minutes cause the decimal is the percentage of the hour, so this
        # is the only way to get an invalid minute value
        result = api.get_time("3.110")
        self.assertEqual(result, None)