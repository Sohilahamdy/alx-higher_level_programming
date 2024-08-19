#!/usr/bin/python3
"""Script to create a State and a City in the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from model_base import Base

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_cities.py <mysql username> <mysql password> <database name>")
        return

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine and bind it to the Base metadata
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}")

    # Create tables if they do not exist
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State and City
    state = State(name="California")
    city = City(name="San Francisco", state=state)

    # Add the State and City to the session and commit
    session.add(state)
    session.add(city)
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
