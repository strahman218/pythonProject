from api import api
import unittest

class TestGetLocationType(unittest.TestCase):
    def test_get_location_type_empty(self):
        result = api.get_location_type()
        self.assertEqual(result, None)

    def test_get_location_type_null(self):
        result = api.get_location_type(None)
        self.assertEqual(result, None)

    def test_get_location_type_int(self):
        result = api.get_location_type(123)
        self.assertEqual(result, None)

    def test_get_location_type_int_string(self):
        result = api.get_location_type("123")
        self.assertEqual(result, 'address')

    def test_get_location_type_valid_lat(self):
        result = api.get_location_type("123, 456")
        self.assertEqual(result, 'latlng')

    def test_get_location_type_valid_address(self):
        result = api.get_location_type('Seattle, WA')
        self.assertEqual(result, 'address')