from unittest import TestCase

import mocks
from helpers import radius_finder


class Test(TestCase):

    def setUp(self):
        self.mock_stores_data = mocks.load_store_data()

    def test_get_stores_in_postcode_radius_with_valid_postcode(self):
        postcode = "SW1A 1AA"
        radius = 10
        stores_result = radius_finder.get_stores_in_postcode_radius(postcode, radius, self.mock_stores_data)
        self.assertEqual(len(stores_result), 5)

    def test_get_stores_in_postcode_radius_with_invalid_postcode(self):
        postcode = 123456
        radius = 10
        stores_result = radius_finder.get_stores_in_postcode_radius(postcode, radius, self.mock_stores_data)
        self.assertEqual(len(stores_result), 0)

    def test_get_stores_in_postcode_radius_with_invalid_radius(self):
        postcode = "SW1A 1AA"
        radius = '10'
        stores_result = radius_finder.get_stores_in_postcode_radius(postcode, radius, self.mock_stores_data)
        self.assertEqual(len(stores_result), 0)

    def test_get_stores_in_postcode_radius_with_invalid_stores_data(self):
        postcode = "SW1A 1AA"
        radius = 10
        stores_result = radius_finder.get_stores_in_postcode_radius(postcode, radius, 'mock_stores_data')
        self.assertEqual(len(stores_result), 0)

    def test_get_stores_in_postcode_radius_with_invalid_postcode_and_radius(self):
        postcode = 123456
        radius = '10'
        stores_result = radius_finder.get_stores_in_postcode_radius(postcode, radius, self.mock_stores_data)
        self.assertEqual(len(stores_result), 0)

    def test_get_stores_in_postcode_radius_with_invalid_postcode_and_stores_data(self):
        postcode = 123456
        radius = 10
        stores_result = radius_finder.get_stores_in_postcode_radius(postcode, radius, 'mock_stores_data')
        self.assertEqual(len(stores_result), 0)

    def test_get_stores_in_postcode_radius_with_invalid_radius_and_stores_data(self):
        postcode = "SW1A 1AA"
        radius = '10'
        stores_result = radius_finder.get_stores_in_postcode_radius(postcode, radius, 'mock_stores_data')
        self.assertEqual(len(stores_result), 0)

    def test_get_stores_in_postcode_radius_with_invalid_postcode_and_radius_and_stores_data(self):
        postcode = 123456
        radius = '10'
        stores_result = radius_finder.get_stores_in_postcode_radius(postcode, radius, 'mock_stores_data')
        self.assertEqual(len(stores_result), 0)