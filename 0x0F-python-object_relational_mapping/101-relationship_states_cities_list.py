#!/usr/bin/python3
"""Script to list all State objects and corresponding City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from model_base import Base

def main():
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py <mysql username> <mysql password> <database name>")
        return

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine and bind it to the Base metadata
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all states
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")
        # Query cities for the current state
        cities = session.query(City).filter(City.state_id == state.id).order_by(City.id).all()
        for city in cities:
            print(f"    {city.id}: {city.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
