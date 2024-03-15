import sqlite3
import db

def connect_sqlite_db(path):
    return sqlite3.connect(path);

"""

"""
def extract_db_data_reservation():
    conn = connect_sqlite_db("../dataset/Phase#1_data/reservations.db")
    cur = conn.cursor()
    # cur.execute("SELECT name FROM sqlite_master WHERE type='table';") reserve table
    ''' cur.execute(f"PRAGMA table_info(reserve);")
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


def extract_db_data_room():
    conn = connect_sqlite_db("../dataset/Phase#1_data/rooms.db")
    cur = conn.cursor()
    # cur.execute("SELECT name FROM sqlite_master WHERE type='table';") Room table
    
    '''cur.execute(f"PRAGMA table_info(Room);")
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


# Load