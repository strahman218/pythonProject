from api import api
import unittest

class TestGetDistance(unittest.TestCase):
    def test_get_distance_both_null(self):
        result = api.get_distance(None, None)
        self.assertEqual(result, None)

    def test_get_distance_both_empty_dict(self):
        result = api.get_distance({}, {})
        self.assertEqual(result, None)

    def test_get_distance_one_null(self):
        result = api.get_distance(None, "Seattle, WA")
        self.assertEqual(result, None)

    def test_get_distance_two_strings(self):
        result = api.get_distance("Seattle, WA", "Boston, MA")
        self.assertEqual(result, None)

    def test_get_distance_two_numbers(self):
        result = api.get_distance(123, 456)
        self.assertEqual(result, None)

    def test_get_distance_misformatted_input(self):
        location1 = {'lat': 123, 'lng': 456}
        location2 = {'lat': 900, 'lng': 839}
        result = api.get_distance(location1, location2)
        self.assertEqual(result, None)

    def test_get_distance_valid_input(self):
        location1 = {'lat': 0, 'lng': 0}
        location2 = {'lat': 0, 'lng': 0}
        result = api.get_distance(location1, location2)
        self.assertEqual(result, 0)

    def test_get_distance_valid_input_2(self):
        location1 = {'lat': 32.9697, 'lng': -96.803}
        location2 = {'lat': 29.467, 'lng': -98.535}
        result = api.get_distance(location1, location2)
        self.assertEqual(result, 262.83141894309045)
