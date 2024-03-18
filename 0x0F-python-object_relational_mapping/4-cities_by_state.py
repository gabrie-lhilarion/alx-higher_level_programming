#!/usr/bin/python3

import MySQLdb
import sys

def list_cities(username, password, database):
    """
    Connects to MySQL, lists all cities from the specified database with their respective states.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing the cities and states tables.

    Returns:
        None. Prints the list of cities with their respective states to the console.
    """
    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = connection.cursor()

        # Construct SQL query with JOIN
        query = """
            SELECT cities.id, cities.name, states.name 
            FROM cities 
            JOIN states ON cities.state_id = states.id 
            ORDER BY cities.id ASC
        """

        # Execute query
        cursor.execute(query)

        # Fetch all results
        cities = cursor.fetchall()

        # Display results
        for city in cities:
            print(city)

        # Close cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Call the list_cities function with provided arguments
    list_cities(username, password, database)
