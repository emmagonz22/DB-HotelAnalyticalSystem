from .db import database


uri = "postgres://mczezvedpbzqiy:6a0a49ce1b57d13cf7c2f17aa352c7258598212c4d3fdf18f27c05ca7ad47f7e@ec2-35-169-9-79.compute-1.amazonaws.com:5432/d4bb9ff0fkont9"

db = database(uri)

def get_connection():
    if db.conn:
        return db.conn
    print(f"Database not connected")
        
def get_cursor():
    if db.conn:
        return db.conn.cursor()
    print(f"Database not connected")
        
