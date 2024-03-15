from .db import database

host = "127.0.0.1"
username = "emmanuel"
password = "dbproject123456789"
dbname = "hotelanalyticssystems" 
port = "5432"

db = database(host,
            username,
            password,
            dbname,
            port)

def get_connection():
    if db.conn:
        return db.conn
    print(f"Database not connected")
        
def get_cursor():
    if db.conn:
        return db.conn.cursor()
    print(f"Database not connected")
        
