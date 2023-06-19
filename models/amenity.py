#!/usr/bin/python3
"""
Defines one class, `Amenity(),
Sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place/house.
    """
    
    name = ""
