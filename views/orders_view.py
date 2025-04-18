import sqlite3
import json

def list_orders():
    """
    Function to query database for all Order records
    and serialize the returned records into json to return to the client

    Returns: json-serialized list of Order dictionary
    """
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT
                    o.id,
                    o.metal_id,
                    o.size_id,
                    o.style_id
                FROM `Orders` o
            """
        )
        query_results = db_cursor.fetchall()

        orders = []
        for row in query_results:
            orders.append(dict(row))
        
        serialized_orders = json.dumps(orders)

        return serialized_orders

def retrieve_order(pk):
    """
    Function to query database for a single Order record
    and serialize the returned Order record into json to return to the client

    Returns: json-serialized dictionary of Order matching pk provided by the client in the request url
    """
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                SELECT
                    o.id,
                    o.metal_id,
                    o.size_id,
                    o.style_id
                FROM `Orders` o
                WHERE o.id = ?
            """, (pk,)
        )

        query_results = db_cursor.fetchone()

        serialized_order = json.dumps(dict(query_results))

        return serialized_order

def create_order(order_data):
    """
    Function to create a new Order record in the database when a client
    POST request is sent with the data send in by the client in the request body

    Returns: True if new row is created in database and False if not
    """
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
                INSERT INTO `Orders` (metal_id, size_id, style_id)
                VALUES (?, ?, ?)
            """,
            (order_data['metal_id'], order_data['size_id'], order_data['style_id'])
        )

        rows_affected = db_cursor.rowcount

        return True if rows_affected > 0 else False


        