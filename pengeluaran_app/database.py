import sqlite3
import pandas as pd

from konfigurasi import DB_PATH


def get_db_connection():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    return conn


def execute_query(query, params=None):

    conn = get_db_connection()

    cursor = conn.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    conn.commit()

    last_id = cursor.lastrowid

    conn.close()

    return last_id


def fetch_query(query, params=None):

    conn = get_db_connection()

    cursor = conn.cursor()

    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_dataframe(query):

    conn = get_db_connection()

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df