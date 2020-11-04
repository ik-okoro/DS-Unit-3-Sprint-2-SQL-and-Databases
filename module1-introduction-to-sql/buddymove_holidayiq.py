import sqlite3
import pandas as pd
import warnings
from query import BUDDY_QUERY_LIST


def connect_to_db(db_name = "buddymove_holidayiq.sqlite3"):
    """
    Function to connect/insantiate a SQLite database
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

# Read in dataframe
df = pd.read_csv("buddymove_holidayiq.csv")


# Hide warning for spaces in columns
#def fxn():
    #warnings.warn("Column spaces", UserWarning)

#with warnings.catch_warnings():
    #warnings.simplefilter("ignore")
    #fxn()

if __name__ == "__main__":
    sql_conn = connect_to_db()
    sql_curs = sql_conn.cursor()

    # Already a user id so set index to False
    df.to_sql(name = "review", con = sql_conn, if_exists = "replace", index = False)
    
    results = execute_query(sql_curs, BUDDY_QUERY_LIST)

    # Results
    print(f"\nNumber of rows: {results[0][0][0]}")
    print(f"Number of users with minimum 100 in Nature & Shopping: {results[1][0][0]}")
    print("\nAVERAGE NUMBER OF REVIEWS")
    print(f"Average Sports reviews: {results[2][0][0]}")
    print(f"Average Religious reviews: {results[2][0][1]}")
    print(f"Average Nature reviews: {results[2][0][2]}")
    print(f"Average Theatre reviews: {results[2][0][3]}")
    print(f"Average Shopping reviews: {results[2][0][4]}")
    print(f"Average Picnic reviews: {results[2][0][5]}")