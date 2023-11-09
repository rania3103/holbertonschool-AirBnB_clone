#!/usr/bin/python3
"""testing Amenity"""
import unittest
from models.amenity import Amenity


class testAmenity(unittest.TestCase):
    """testing"""

    def test_value(self):
        """test value of attribute name"""
        inst = Amenity(name="hello")
        self.assertEqual(inst.name, "hello")

    def test_type(self):
        """test type of attribute name"""
        inst = Amenity(name="hello")
        self.assertIsInstance(inst.name, str)


if __name__ == "__main__":
    unittest.main()
