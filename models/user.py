#!/usr/bin/python3
"""Write a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """this is the class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
