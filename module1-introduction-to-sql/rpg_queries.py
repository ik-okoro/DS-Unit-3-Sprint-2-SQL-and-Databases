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


if __name__ == "__main__":
    # Connect to DB
    sql_conn = connect_to_db()
    # Create cursor
    sql_curs = sql_conn.cursor()
    results = execute_query(sql_curs, QUERY_LIST)

    # Print results
    print("--------------SUMMARY--------------")
    print(f"Total characters: {results[0][0][0]}")
    print("\nSUBCLASSES")
    print(f"Total Mages: {results[1][0][0]}")
    print(f"Total Thieves: {results[2][0][0]}")
    print(f"Total Clerics: {results[3][0][0]}")
    print(f"Total Fighters: {results[4][0][0]}\n")
    print("ITEMS")
    print(f"Total items: {results[5][0][0]}")
    print(f"Total weapons: {results[6][0][0]}")
    print(f"Total Non-Weapons: {results[7][0][0]}")
    print("\nCHARACTER ITEMS")
    print(f"Number of items for first 20 characters: {results[8][:][:]}")
    print(f"Number of weapons for first 20 characters: {results[9][:][:]}")
    print("\nAVERAGE CHARACTER ITEMS")
    print(f"Average items per character: {results[10][0][0]}")
    print(f"Average weapons per character: {results[11][0][0]}")
    