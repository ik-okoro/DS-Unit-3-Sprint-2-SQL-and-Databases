import sqlite3

def connect_to_db(db_name = "rpg_db.sqlite3"):
    """
    Function to connect to a SQL database
    """
    return sqlite3.connect(db_name)

def execute_query(cursor, query):
    """
    Function to execute a given query
    """
    cursor.execute(query)
    return cursor.fetchall()

GET_CHARACHTERS = """
SELECT * 
FROM charactercreator_character;
"""

if __name__ == "__main__":
    # Connect to DB
    conn = connect_to_db()
    # Create cursor
    curs = conn.cursor()
    results = execute_query(curs, GET_CHARACHTERS)
    print(results[0])