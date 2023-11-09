#!/usr/bin/python3
"""testing user"""
import unittest
from models.user import User


class testUser(unittest.TestCase):
    """this is the class fo testing"""

    def test_value(self):
        """test values of attributes"""
        inst = User(
            email="hh@gmail.com",
            password="123",
            first_name="hello",
            last_name="world")
        self.assertEqual(inst.email, "hh@gmail.com")
        self.assertEqual(inst.password, "123")
        self.assertEqual(inst.first_name, "hello")
        self.assertEqual(inst.last_name, "world")

    def test_type(self):
        """test types of attributes"""
        inst = User()
        self.assertIsInstance(inst.email, str)
        self.assertIsInstance(inst.password, str)
        self.assertIsInstance(inst.first_name, str)
        self.assertIsInstance(inst.last_name, str)


if __name__ == "__main__":
    unittest.main()
