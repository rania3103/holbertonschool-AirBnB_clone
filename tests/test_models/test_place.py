#!/usr/bin/python3
"""testing Place"""
import unittest
from models.place import Place


class testPlace(unittest.TestCase):
    """testing"""

    def test_type(self):
        """test type of attribute name"""
        inst = Place()
        self.assertIsInstance(inst.city_id, str)
        self.assertIsInstance(inst.user_id, str)
        self.assertIsInstance(inst.name, str)
        self.assertIsInstance(inst.description, str)
        self.assertIsInstance(inst.number_rooms, int)
        self.assertIsInstance(inst.number_bathrooms, int)
        self.assertIsInstance(inst.max_guest, int)
        self.assertIsInstance(inst.price_by_night, int)
        self.assertIsInstance(inst.latitude, float)
        self.assertIsInstance(inst.longitude, float)
        self.assertIsInstance(inst.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
