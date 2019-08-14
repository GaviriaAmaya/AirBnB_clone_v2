#!/usr/bin/python3
"""This is the city class"""
from Base, models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, DateTime


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
