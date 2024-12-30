import sqlite3
import pandas as pd

#pad naar database maken, sqllite gebruikt dit was de gemakkelijkste manier
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


#aanmaken data tabel in db met de dataset kolommen
def create_table(conn):
    sql_create_table = """ CREATE TABLE IF NOT EXISTS comments (
                                COMMENT_ID text PRIMARY KEY,
                                AUTHOR text NOT NULL,
                                DATE text,
                                CONTENT text,
                                CLASS integer
                            ); """
    cursor = conn.cursor()
    cursor.execute(sql_create_table)


#insteken data
def insert_data(conn, df):
    cursor = conn.cursor()
    df.to_sql('comments', conn, if_exists='replace', index=False)

#queryen data
def load_data_from_db(conn):
    query = "SELECT * FROM comments"
    df = pd.read_sql_query(query, conn)
    return df
