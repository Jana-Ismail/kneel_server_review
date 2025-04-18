import sqlite3
import json

def list_metals():
    """
    Function to query the database for a list of all Metal records
    and serialize the data into json to return to the client

    Returns: json-serialized list of metal dictionaries
    """
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                m.id,
                m.metal,
                m.price
            FROM Metals m
        """)
        query_results = db_cursor.fetchall()

        metals = []
        for row in query_results:
            metals.append(dict(row))
        
        serialized_metals = json.dumps(metals)

        return serialized_metals



def retrieve_metal(pk):
    """
    Function to query the database for a single Metal record
    and serialize the data into json to return to the client

    Returns: json-serialized dictionary of a single Metal record
    """
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT
                    m.id,
                    m.metal,
                    m.price
                FROM Metals m
                WHERE m.id = ?
            """, (pk,)
        )

        query_results = db_cursor.fetchone()

        serialized_metal = json.dumps(dict(query_results))

        return serialized_metal