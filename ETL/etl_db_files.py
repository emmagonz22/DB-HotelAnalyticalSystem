import sqlite3
from database import db, get_connection, get_cursor
from collections import defaultdict
def connect_sqlite_db(path):
    return sqlite3.connect(path);

# Room data (Hashmap is used to access the data with room id to transform data) (For transformed data)

room_dict_data = defaultdict()

# Reservation data (Hashmap is used to access the data with reserve id to transform data) (For transformed data)

reserve_dict_data = defaultdict()

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
## All the data from both tables
room_data = extract_db_data_room()
reserve_data = extract_db_data_reservation()

def transform_room_data():
    for row in room_data: 
       room_data[row[0]] = row
def transform_reserve_data():
    # Needs to load the RoomDescription data to verify that "Clients can only reserve a room with equal or less gests than the room's capacity"
    for row in reserve_data:
        # Verify if the price is correct? rprice(room) * (number_of_days)[end_date - start date] (RoomUnavailable)?
        # Verify for valid payment method 
        if row[4] in ["cash", "check", "credit card", "debit card", "pear pay"]: 
            # add row id as key and entire row as value
            reserve_dict_data[row[0]] = row

#transform call 
transform_room_data()
transform_reserve_data()

# Load
def load_room_data():
    db.connect()
    conn = get_connection()
    cur = get_cursor()
    
    for row in room_dict_data.values():
        cur.execute('INSERT INTO reserve (rid, hid, rdid, rprice) VALUES (%s, %s, %s, %s);', row)

    conn.commit()
    db.disconnect()


def load_reservation_data():
    db.connect()
    conn = get_connection()
    cur = get_cursor()
    data = extract_db_data_reservation()

    for row in reserve_dict_data.values():
        # Verify for valid payment method
        if row[4] not in ["cash", "check", "credit card", "debit card", "pear pay"]: 
            print("Invalid row", row)
        ## Compare with room capacity using id
        else:
            print("Inserting: ", row)
            # add error handling
            cur.execute('INSERT INTO reserve (reid, ruid, clid, total_cost, payments, guests) VALUES (%s, %s, %s, %s, %s, %s);', row)

    conn.commit()
    db.disconnect()

if __name__ == "__main__":
    load_reservation_data()
