#!/usr/bin/python3

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Connects to a MySQL database and lists all states.

    This function connects to a MySQL server using the provided username,
    password, and database name. It executes a SQL query to retrieve all
    states from the 'states' table in the database, orders them by ID
    in ascending order, fetches all results, and prints them to the console.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the MySQL database.

    Returns:
        None
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

        # Execute query to retrieve all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all results
        states = cursor.fetchall()

        # Display results
        for state in states:
            print(state)

        # Close cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the list_states function with provided arguments
    list_states(username, password, database)

