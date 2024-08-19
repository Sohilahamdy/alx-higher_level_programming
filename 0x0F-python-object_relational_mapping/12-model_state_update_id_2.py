#!/usr/bin/python3
"""Updates the name of a State object with id = 2 in the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Ensure the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>")
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

    # Query the State object with id = 2
    state = session.query(State).filter(State.id == 2).one_or_none()

    if state:
        # Update the state's name
        state.name = "New Mexico"

        # Commit the change
        session.commit()
