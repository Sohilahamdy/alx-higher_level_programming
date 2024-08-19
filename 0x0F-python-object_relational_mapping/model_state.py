#!/usr/bin/python3
"""Defines the State class and creates the states table in the database."""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship  # Import relationship here
import sys

Base = declarative_base()

class State(Base):
    """State class for the MySQL table states."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Relationship with City class
    cities = relationship("City", back_populates="state")

if __name__ == "__main__":
    # Ensure that all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./model_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Get arguments from command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine connected to the specified MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost/{database_name}', pool_pre_ping=True)

    # Create the tables in the database
    Base.metadata.create_all(engine)
