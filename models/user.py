#!/usr/bin/python3
"""This is the user class"""


import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5



class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    if models.storage_t == 'db':
        __tablename__ = "users"

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        address = Column(String(128))
        photo = Column(String(128))
        rating = Column(int, default=0)
        orders = relationship("Order", cascade='all, delete, delete-orphan',
                            backref="user")
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                            backref="user")

    else:

        email = ""
        password = ""
        first_name = ""
        last_name = ""
        phone = ""
        address = ""
        rating = 0
        photo = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)