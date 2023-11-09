#!/usr/bin/python3
"""class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """this is the class review"""
    place_id = ""
    user_id = ""
    text = ""
