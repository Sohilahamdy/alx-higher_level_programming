#!/usr/bin/python3
"""Print the first State object from the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Ensure the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Retrieve command-line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine connected to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost/{database_name}', pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a session instance
    session = Session()

    # Query for the first State object, sorted by id
    state = session.query(State).order_by(State.id).first()

    # Check if a state was found and print the result
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")
