#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship('Place', secondary=place_amenity)
