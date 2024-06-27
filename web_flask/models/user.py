#!/usr/bin/python3
"""This is the user class"""

from app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel, Base
from hashlib import md5



class User(BaseModel, Base):
    
    __tablename__ = "users"
        
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.Text, nullable=True)
    last_name = db.Column(db.Text, nullable=True)
    phone_number = db.Column(db.Text, nullable=True)
    address = db.Column(db.Text, nullable=True)

    orders = db.relationship("Order", cascade='all, delete, delete-orphan', backref="user")
    reviews = db.relationship("Review", cascade='all, delete, delete-orphan', backref="user")
        
    

    def __repr__(self):
        return f'person with name {self.first_name} and email {self.email}'


    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)