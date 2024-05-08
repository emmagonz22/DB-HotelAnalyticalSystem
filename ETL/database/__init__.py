from .db import database


uri = "postgres://vaccmbbtflaoyw:cec952ce84d6a3824ee8815c1784bab847d052cf2efa4e71f0f1b263e1eae69b@ec2-18-213-181-126.compute-1.amazonaws.com:5432/dov2laco77h6n"

db = database(uri)

def get_connection():
    if db.conn:
        return db.conn
    print(f"Database not connected")
        
def get_cursor():
    if db.conn:
        return db.conn.cursor()
    print(f"Database not connected")
        
