#!/usr/bin/python3

import MySQLdb
import sys


def search_states(username, password, database, state_name):
    """
    Connects to MySQL, searches for specified state name in states table.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing the states table.
        state_name (str): Name of the state to search for.

    Returns:
        None. Prints the matching states to the console.
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

        # Construct SQL query
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        # Execute query with user input
        cursor.execute(query, (state_name,))

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
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the search_states function with provided arguments
    search_states(username, password, database, state_name)
