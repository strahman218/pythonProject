from api import api
import unittest

class TestGetLocationData(unittest.TestCase):
    def test_get_location_data_valid_input(self):
        location1 = "Seattle, WA"
        location2 = "Tampa, FL"
        speed = 10.5

        result = api.get_location_data(location1, location2, speed)
        results = {'location1': 'Seattle, WA, USA', 'location2': 'Tampa, FL, USA', 'lat': 47.6062095, 'lng': -122.3320708,
                   'lat2': 47.6062095, 'lng2': -122.3320708, 'distance': '2526.88', 'hour': 240, 'minutes': 40}
        self.assertEqual(result, results)


    def test_get_location_data_zero_results(self):
        location1 = "Boston, MA"
        location2 = "Sarafland, NZ"
        speed = 7.5

        result = api.get_location_data(location1, location2, speed)
        self.assertEqual(result, {})


    def test_get_location_data_check_default_speed(self):
        location1 = "Boston, MA"
        location2 = "Quincy, MA"

        result = api.get_location_data(location1, location2)
        results = {'location1': 'Boston, MA, USA', 'location2': 'Quincy, MA, USA', 'lat': 42.3600825, 'lng': -71.0588801,
                   'lat2': 42.3600825, 'lng2': -71.0588801, 'distance': '7.95', 'hour': 2, 'minutes': 16}
        self.assertEqual(result, results)


    def test_get_location_data_none(self):
        result = api.get_location_data(None, None, None)
        self.assertEqual(result, {})


    def test_get_location_data_empty(self):
        result = api.get_location_data()
        self.assertEqual(result, {})


    def test_get_location_data_empty_string(self):
        result = api.get_location_data("", "", 5.0)
        self.assertEqual(result, {})
