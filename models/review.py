#!/usr/bin/python3
'''
    Implementation of the Review class
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


storage_type = getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    '''
        Implementation for the Review.
    '''
    __tablename__ = 'reviews'
    if storage_type == 'db':
        place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
