import sqlite3
from query import QUERY_LIST

def connect_to_db(db_name = "rpg_db.sqlite3"):
    """
    Function to connect to a SQL database
    """
    return sqlite3.connect(db_name)

def execute_query(cursor, queries):
    """
    Function to execute a given query
    Pass queries in a list
    """
    results = []
    for query in queries:
        cursor.execute(query)
        results.append(cursor.fetchall())
    return results

GET_CHARACTERS = """
SELECT * 
FROM charactercreator_character;
"""

if __name__ == "__main__":
    # Connect to DB
    conn = connect_to_db()
    # Create cursor
    curs = conn.cursor()
    results = execute_query(curs, QUERY_LIST)
    print(results[0][0])