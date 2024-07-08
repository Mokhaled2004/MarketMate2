#!/usr/bin/python3
"""This is the review class"""


import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel,Base):

    """Represents a review """

    if models.storage_t == 'db':

        __tablename__ = "reviews"


        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        text = Column(String(1024), nullable=False)

    else:
        user_id = ""
        subject = ""
        text = ""
        


    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)