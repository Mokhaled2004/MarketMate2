#!/usr/bin/python3
"""This is the review class"""

from app import db
from sqlalchemy import Column, Integer, String
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel,Base):
    
    """Represents a review """
    
    

    __tablename__ = "reviews"

    
    user_id = db.Column(db.String(60), db.ForeignKey("users.id"), nullable=False)
    text = db.Column(db.String(1024), nullable=False)


    


    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)