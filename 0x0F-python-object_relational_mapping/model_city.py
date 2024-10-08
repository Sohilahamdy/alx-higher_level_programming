#!/usr/bin/python3
"""Define the City class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    """Represents a city for a MySQL database."""
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # Define relationship with State
    state = relationship("State", back_populates="cities")
