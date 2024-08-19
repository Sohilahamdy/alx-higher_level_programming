#!/usr/bin/python3
"""Script to list all City objects and their corresponding State objects"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State
from model_base import Base

def main():
    if len(sys.argv) != 4:
        print("Usage: ./102-relationship_cities_states_list.py <mysql username> <mysql password> <database name>")
        return

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine and bind it to the Base metadata
    engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_pass}@localhost:3306/{db_name}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all cities and their associated states
    cities = session.query(City).order_by(City.id).all()

    # Display the results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    main()
