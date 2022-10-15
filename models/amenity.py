#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

s = "HBNB_TYPE_STORAGE"


class Amenity(BaseModel, Base):
    """defines the amenity class"""
    __tablename__ = 'amenities'
    if s in environ.keys() and getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
