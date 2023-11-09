#!/usr/bin/python3
"""testing Review"""
import unittest
from models.review import Review


class testReview(unittest.TestCase):
    """testing"""

    def test_type(self):
        """test type of attribute name"""
        inst = Review()
        self.assertIsInstance(inst.place_id, str)
        self.assertIsInstance(inst.user_id, str)
        self.assertIsInstance(inst.text, str)


if __name__ == "__main__":
    unittest.main()
