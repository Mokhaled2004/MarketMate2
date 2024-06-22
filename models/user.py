#!/usr/bin/python3
"""Defines the User class."""

from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from hashlib import md5
import models




class User(BaseModel, Base):
    
    """Represents a user for the application."""
    if models.storage_t == 'db':

        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        phone_number = Column(String(20), nullable=True)
        address = Column(String(256), nullable=True)
        orders = relationship("order", cascade='all,delete,delete-orphan',backref="user")
        reviews = relationship("review",cascade='all,delete,delete-orphan', backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        phone_number = ""
        address = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
    
    
    
