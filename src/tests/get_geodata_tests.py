from api import api
import unittest


class TestGeodata(unittest.TestCase):
    def test_get_geodata_valid_input(self):
        location = "Boston, MA"
        result = api.get_geodata(location)
        self.assertEqual(result,{'lat': 42.3600825, 'lng': -71.0588801, 'address': "Boston, MA, USA"})

    def test_get_geodata_location_null(self):
        result = api.get_geodata(None)
        self.assertEqual(result, None)

    def test_get_geodata_location_int(self):
        result = api.get_geodata(123)
        self.assertEqual(result, None)

    def test_get_geodata_location_empty(self):
        result = api.get_geodata()
        self.assertEqual(result, None)

    def test_get_geodata_location_fake_loc(self):
        result = api.get_geodata('sarafland')
        self.assertEqual(result, None)






