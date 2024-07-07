#!/usr/bin/python3
"""This is the Payment class"""


import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey


class Payment(BaseModel,Base):

    """Represents a payment """

    if models.storage_t == 'db':

        __tablename__ = "payments"


        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        order_id = Column(String(60), ForeignKey("orders.id"), nullable=False)
        payment_type = Column(String(1024), nullable=False)

    else:
        user_id = ""
        order_id = ""
        payment_type = ""
        card_number = ""
        card_name = ""
        expiry_month= ""
        expiry_year= ""
        cvv= ""
        


    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)