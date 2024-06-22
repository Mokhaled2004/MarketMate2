#!/usr/bin/python3
"""Defines the Review class."""
from sqlalchemy.ext.declarative import declarative_base
from Models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

class Review(BaseModel):
    
    """Represents a review """
    
    
    __tablename__ = "reviews"

    review_id = Column(Integer, primary_key=True, nullable=False)
    text = Column(String(1024), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    rating = Column(Float, nullable=False)
    
 
