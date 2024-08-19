#!/usr/bin/python3
"""State model"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_base import Base

class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=False)

    # Define the relationship to City
    cities = relationship("City", back_populates="state")
