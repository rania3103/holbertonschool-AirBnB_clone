#!/usr/bin/python3
"""testing state"""
import unittest
from models.state import State


class testState(unittest.TestCase):
    """testing"""

    def test_value(self):
        """test value of attribute name"""
        inst = State(name="hello")
        self.assertEqual(inst.name, "hello")

    def test_type(self):
        """test type of attribute name"""
        inst = State(name="hello")
        self.assertIsInstance(inst.name, str)


if __name__ == "__main__":
    unittest.main()
