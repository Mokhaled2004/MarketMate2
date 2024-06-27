#!/usr/bin/python3
"""This is the order class"""


import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, Table, String, Integer, ForeignKey
from sqlalchemy.orm import relationship



<<<<<<< HEAD
if models.storage_t == 'db':
    order_product = Table('order_product', Base.metadata,
                      Column('order_id', String(60), ForeignKey('orders.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True),
                      Column('product_id', String(60), ForeignKey('products.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True))
=======
class OrderProduct(Base):
    __tablename__ = 'order_product'

    order_id = db.Column(db.String(60), db.ForeignKey('orders.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    product_id = db.Column(db.String(60), db.ForeignKey('products.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
>>>>>>> 641ae9be66fa60881ee61d6b2ac76b1fd3c04341


class Order(BaseModel, Base):
    """Representation of Order"""
    if models.storage_t == 'db':
        __tablename__ = 'orders'
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        market_name = Column(String(128), nullable=False)
        products = relationship("Product", secondary=order_product, back_populates="orders")

<<<<<<< HEAD
    else:
=======
    id = db.Column(db.String(60), primary_key=True)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    market_name = db.Column(db.String(128), nullable=False)
>>>>>>> 641ae9be66fa60881ee61d6b2ac76b1fd3c04341

        user_id = ""
        market_name = ""
        products_ids = []

    def __init__(self, *args, **kwargs):
        """initializes Order"""
        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        
        @property
        def products(self):
            """getter attribute returns the list of Product instances"""
            from models.product import Product
            product_list = []
            all_products = models.storage.all(Product)
            for product in all_products.values():
                if product.order_id == self.id:
                    product_list.append(product)
            return product_list