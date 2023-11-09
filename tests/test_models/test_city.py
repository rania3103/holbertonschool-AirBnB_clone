#!/usr/bin/python3
"""testing City"""
import unittest
from models.city import City


class testCity(unittest.TestCase):
    """testing"""

    def test_value(self):
        """test values of attributes"""
        inst = City(state_id="123", name="hello")
        self.assertEqual(inst.name, "hello")
        self.assertEqual(inst.state_id, "123")

    def test_type(self):
        """test type of attributes"""
        inst = City(state_id="123", name="hello")
        self.assertIsInstance(inst.name, str)
        self.assertIsInstance(inst.state_id, str)

if __name__ == "__main__":
    unittest.main()
