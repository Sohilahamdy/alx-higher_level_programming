#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, db_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the rows
    rows = cursor.fetchall()
    
    # Print the rows
    for row in rows:
        print(row)
    
    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Get the arguments from the command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    # Call the function
    list_states(mysql_user, mysql_password, database_name)
