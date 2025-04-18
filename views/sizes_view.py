import sqlite3
import json

def list_sizes():
    """
    Function to query database for all Size records
    Returns: list representation of Size dictionaries
    """
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT
                    s.id,
                    s.carats,
                    s.price
                FROM Sizes s
            """
        )

        query_results = db_cursor.fetchall()

        sizes = []
        for row in query_results:
            sizes.append(dict(row))

        serialized_sizes = json.dumps(sizes)

        return serialized_sizes

def retrieve_size(pk):
    """Function to query database for a single Size record
    Returns: dictionary representation of single Size record
    """
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT
                    s.id,
                    s.carats,
                    s.price
                FROM Sizes s
                WHERE s.id = ?
            """, (pk,)
        )

        query_results = db_cursor.fetchone()

        serialized_size = json.dumps(dict(query_results))

        return serialized_size