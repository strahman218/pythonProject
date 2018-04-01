from api import api
import unittest

class TestDataValidation(unittest.TestCase):
    # *** check_valid_location tests ***
    def test_check_valid_location_both_null(self):
        result = api.check_valid_location(None, None)
        self.assertEqual(result, False)

    def test_check_valid_location_one_null(self):
        result = api.check_valid_location(None, "hello")
        self.assertEqual(result, False)

    def test_check_valid_location_string(self):
        result = api.check_valid_location("hello", "goodbye")
        self.assertEqual(result, False)

    def test_check_valid_location_number(self):
        result = api.check_valid_location(123, 456)
        self.assertEqual(result, False)

    def test_check_valid_location_format(self):
        location1 = {'lat': 'hello', 'lng': 'goodbye'}
        location2 = {'lat': 'hello2', 'lng': 'goodbye2'}
        result = api.check_valid_location(location1, location2)
        self.assertEqual(result, False)

    def test_check_valid_location_invalid_bounds(self):
        location1 = {'lat': 47.101, 'lng': -122.90}
        location2 = {'lat': 109.101, 'lng': -100.90}
        result = api.check_valid_location(location1, location2)
        self.assertEqual(result, False)

    def test_check_valid_location_valid_bounds(self):
        location1 = {'lat': 9.622, 'lng': 13.359}
        location2 = {'lat': -61.698, 'lng': -21.753509}
        result = api.check_valid_location(location1, location2)
        self.assertEqual(result, True)

    # *** check valid bounds tests ***
    def test_check_valid_bounds_null(self):
        result = api.check_valid_bounds(None, None)
        self.assertEqual(result, False)

    def test_check_valid_bound_lat_upper_bound(self):
        result = api.check_valid_bounds(90, 80)
        self.assertEqual(result, False)

    def test_check_valid_bound_lat_lower_bound(self):
        result = api.check_valid_bounds(-90, 39)
        self.assertEqual(result, False)

    def test_check_valid_bound_lng_lower_bound(self):
        result = api.check_valid_bounds(-80, -180)
        self.assertEqual(result, False)

    def test_check_valid_bound_lng_upper_bound(self):
        result = api.check_valid_bounds(-80, 180)
        self.assertEqual(result, False)

    def test_check_valid_bound_both_invalid(self):
        result = api.check_valid_bounds(-200, 900)
        self.assertEqual(result, False)

    def test_check_valid_bound_both_valid(self):
        result = api.check_valid_bounds(84, -179)
        self.assertEqual(result, True)

    def test_check_valid_bound_both_valid_string(self):
        result = api.check_valid_bounds("84", "-179")
        self.assertEqual(result, True)