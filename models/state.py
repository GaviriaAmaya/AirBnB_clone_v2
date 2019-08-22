#!/usr/bin/python3
"""This is the state class"""
from os import getenv
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', backref="state")
    else:
        @property
        def cities(self):
            """ return all cities belonged to self"""

            aux = []
            for key, value in models.storage.all().items():
                if (type(value).__name__ == 'City'):
                    if (hasattr(value, "state_id")):
                        if (value.state_id == self.id):
                            aux.append(value)
            return aux
