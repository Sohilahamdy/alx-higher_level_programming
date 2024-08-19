#!/usr/bin/python3
import MySQLdb
import sys

def safe_filter_states(username, password, db_name, state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Prepare the SQL query with placeholders to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    # Execute the SQL query with the parameterized value
    cursor.execute(query, (state_name,))
    
    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)
    
    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)

    # Get the arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function
    safe_filter_states(mysql_user, mysql_password, database_name, state_name)
