import sqlite3
from database import db, get_connection, get_cursor
from collections import defaultdict
import pandas as pd

def connect_sqlite_db(path):
    return sqlite3.connect(path);


"""
    Extract the data from the SQLite db with table reserve
"""
def extract_db_data_reservation():
    conn = connect_sqlite_db("../dataset/Phase#1_data/reservations.db")
    cur = conn.cursor()
    # cur.execute("SELECT name FROM sqlite_master WHERE type='table';") reserve table -> Display all table
    ''' cur.execute(f"PRAGMA table_info(reserve);")  -> Display columns from table 
        (0, 'reid', 'INT', 0, None, 1)
        (1, 'ruid', 'INT', 0, None, 0)
        (2, 'clid', 'INT', 0, None, 0)
        (3, 'total_cost', 'float', 0, None, 0)
        (4, 'payment', 'TEXT', 0, None, 0)
        (5, 'guests', 'INT', 0, None, 0)
    '''
    cur.execute("SELECT * FROM reserve;")
    data = cur.fetchall()
    conn.close()
    return data

"""
    Extract the data from the SQLite db with table rooms
"""
def extract_db_data_room():
    conn = connect_sqlite_db("../dataset/Phase#1_data/rooms.db")
    cur = conn.cursor()
    # cur.execute("SELECT name FROM sqlite_master WHERE type='table';") Room table -> Display all table
    
    '''cur.execute(f"PRAGMA table_info(Room);") -> Display columns from table 
        (0, 'rid', 'INT', 0, None, 0)
        (1, 'hid', 'INT', 0, None, 0)
        (2, 'rdid', 'INT', 0, None, 0)
        (3, 'rprice', 'float', 0, None, 0)
    '''

    cur.execute("SELECT * FROM Room;")
    data = cur.fetchall()
    conn.close()
    return data


# Transform

## Room data (Panda data frame is used to access the data with room id to transform data) (For transformed data)
room_column = ["rid","hid","rdid","rprice"]
room_data = pd.DataFrame(extract_db_data_room(), columns=room_column)
## Reservation data (Panda dataframe is used to access the data with reserve id to transform data) (For transformed data)
reserve_column = ["reid","ruid","clid","total_cost", "payments", "guests"]
reserve_data = pd.DataFrame(extract_db_data_reservation(), columns=reserve_column)

reserve_data = reserve_data[ reserve_data["payments"].isin(["cash", "check", "credit card", "debit card", "pear pay"]) ]

# Load
def load_room_data():
    db.connect()
    conn = get_connection()
    cur = get_cursor()
    
    if conn is None:
        print("Error conecting to the database")
        return

    for row in room_data.values:
        try:
            cur.execute('INSERT INTO room (rid, hid, rdid, rprice) VALUES (%s, %s, %s, %s);', row)
        except Exception as e:
            print("Error inserting:", e)
            pass
    conn.commit()
    db.disconnect()


def load_reservation_data():
    db.connect()
    conn = get_connection()
    cur = get_cursor()

    if conn is None:
        print("Error conecting to the database")
        return

    for row in reserve_data.values:
        try: 
            print("Inserting: ", row)
            cur.execute('INSERT INTO reserve (reid, ruid, clid, total_cost, payments, guests) VALUES (%s, %s, %s, %s, %s, %s);', row)
        except Exception as e:
            print("Error inserting:", e)
            pass
    conn.commit()
    db.disconnect()

