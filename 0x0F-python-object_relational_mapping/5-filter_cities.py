#!/usr/bin/python3
import MySQLdb
import sys

def list_cities_by_state(username, password, db_name, state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Prepare the SQL query with placeholders
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    
    # Execute the SQL query
    cursor.execute(query, (state_name,))
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Extract city names from the results
    city_names = [row[0] for row in results]
    
    # Print the city names separated by ', '
    print(", ".join(city_names))
    
    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)

    # Get the arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function
    list_cities_by_state(mysql_user, mysql_password, database_name, state_name)
