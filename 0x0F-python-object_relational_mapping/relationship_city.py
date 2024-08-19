#!/usr/bin/python3
"""City model"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_base import Base

class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Define the relationship to State
    state = relationship("State", back_populates="cities")
