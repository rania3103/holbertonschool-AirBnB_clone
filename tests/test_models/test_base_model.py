#!/usr/bin/python3
"""testing testbase"""
from models.base_model import BaseModel
import unittest
from datetime import datetime


class testBaseModel(unittest.TestCase):
    """this is the class for testing"""

    def test_classname(self):
        """test class name"""
        inst = BaseModel()
        self.assertEqual(inst.__class__.__name__, "BaseModel")

    def test_typenumber(self):
        """test type of id"""
        inst = BaseModel()
        self.assertEqual(type(inst.id), str)

    def test_values(self):
        """test values"""
        inst = BaseModel()
        inst.name = "My First Model"
        inst.my_number = 89
        self.assertEqual(inst.name, "My First Model")
        self.assertEqual(inst.my_number, 89)

    def test_typedatetime(self):
        """test type datetime"""
        inst = BaseModel()
        self.assertIsInstance(inst.created_at, datetime)
        self.assertIsInstance(inst.updated_at, datetime)

    def test_id(self):
        """make sure that ids are unique"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertNotEqual(inst1.id, inst2.id)


if __name__ == "__main__":
    unittest.main()
