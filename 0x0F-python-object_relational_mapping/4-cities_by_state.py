#!/usr/bin/python3
import MySQLdb
import sys

def list_cities(username, password, db_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Prepare the SQL query
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    
    # Execute the SQL query
    cursor.execute(query)
    
    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)
    
    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Get the arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the function
    list_cities(mysql_user, mysql_password, database_name)
