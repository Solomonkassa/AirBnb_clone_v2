#!/usr/bin/python3
"""Defines one class, `State()`,
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A state in the application.
    """
    name = ""
