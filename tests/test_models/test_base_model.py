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

    def test_json(self):
        """test dict representation when attributes are set in the creation of the instance"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.id = '56d43177-cc5f-4d6c-a0c1-e167f8c27337'
        my_model.created_at = datetime(2017, 9, 28, 21, 3, 54, 52298)
        my_model.updated_at = datetime(2017, 9, 28, 21, 3, 54, 52302)
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json,
                         {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                          'created_at': '2017-09-28T21:03:54.052298',
                          '__class__': 'BaseModel',
                          'my_number': 89,
                          'updated_at': '2017-09-28T21:03:54.052302',
                          'name': 'My_First_Model'})

    def test_kwargs(self):
        """test dict representation when attributes are set using kwargs"""
        inst = BaseModel(
            id="11",
            created_at="2017-09-28T21:03:54.052298",
            my_number=89,
            updated_at="2017-09-28T21:03:54.052302",
            name="My_First_Model")
        dtobj_created_at = datetime.strptime(
            "2017-09-28T21:03:54.052298", "%Y-%m-%dT%H:%M:%S.%f")
        dtobj_updated_at = datetime.strptime(
            "2017-09-28T21:03:54.052302", "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(inst.id, "11")
        self.assertEqual(inst.created_at, dtobj_created_at)
        self.assertEqual(inst.my_number, 89)
        self.assertEqual(inst.updated_at, dtobj_updated_at)
        self.assertEqual(inst.name, "My_First_Model")


if __name__ == "__main__":
    unittest.main()
