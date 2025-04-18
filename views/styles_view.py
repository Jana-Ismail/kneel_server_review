import sqlite3
import json

def list_styles():
    """
    Function to query database for all Style records
    and serialize the Style data to return to the client
    
    Returns: list representation of Style dictionaries
    """
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT
                    st.id,
                    st.style,
                    st.price
                FROM Styles st
            """ 
        )

        query_results = db_cursor.fetchall()

        styles = []
        for row in query_results:
            styles.append(dict(row))
        
        serialized_styles = json.dumps(styles)

        return serialized_styles

def retrieve_style(pk):
    """
    Function to query the database for a single Style record with the id
    matching the pk passed in && serialize the Style data to return to the client

    Returns: dictionary representation of Style record
    """
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT
                    st.id,
                    st.style,
                    st.price
                FROM Styles st
                WHERE st.id = ?
            """, (pk,)
        )
        query_results = db_cursor.fetchone()

        serialized_style = json.dumps(dict(query_results))

        return serialized_style