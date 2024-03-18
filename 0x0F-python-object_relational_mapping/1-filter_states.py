import MySQLdb
import sys

def list_states_starting_with_N(username, password, database):
    """
    Connects to MySQL, lists states starting with 'N' from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the MySQL database containing the states table.

    Returns:
        None. Prints the list of states starting with 'N' to the console.
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

        # Execute query
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

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
    
    # Call the list_states_starting_with_N function with provided arguments
    list_states_starting_with_N(username, password, database)
