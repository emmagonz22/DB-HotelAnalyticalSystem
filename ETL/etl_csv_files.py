import pandas as pd
from database import db, get_connection, get_cursor


# Extract
def extract_csv(path):
    return pd.read_csv(path)

# Transform
def transform_hotel_csv(unfiltered_data):
    renamed_data = unfiltered_data.rename(columns={'chid': 'chain', 
                                                    'hname': 'name', 
                                                    'hcity': 'city'})
    filtered_data = renamed_data.dropna()
    return filtered_data


def transform_client_csv(unfiltered_data):
    renamed_data = unfiltered_data.rename(columns={
        'clid' : "clid",
        'fname' : 'fname',
        'lname' : 'lastname',
        'age' : 'age',
        'memberyear' : 'memberyear'
    })
    filtered_data = renamed_data.dropna()
    return filtered_data

def transform_room_unavailable_csv(unfiltered_data):
    renamed_data = unfiltered_data.rename(columns={
        'ruid' : "ruid",
        'rid' : 'rid',
        'startdate' : 'start_date',
        'enddate' : 'end_date'
    })
    filtered_data = renamed_data.dropna()
    return filtered_data

# Load
def load_hotel_csv():
    db.connect()
    conn = get_connection()
    cur = get_cursor()


    unfiltered_hotel_data = extract_csv("../dataset/Phase#1_data/hotel.csv")
    filtered_hotel_data = transform_hotel_csv(unfiltered_hotel_data)

    for hid, chid, hname, hcity in filtered_hotel_data.values:
        try:
            cur.execute("INSERT into hotel (hid, chid, hname, hcity) VALUES(%s, %s, %s, %s);", (hid, chid, hname, hcity))
        except Exception as e:
            print("An error occurred while inserting into hotel: ", e)
            pass



    conn.commit()
    db.disconnect()

def load_client_csv():

    db.connect()
    conn = get_connection()
    cur = get_cursor()

    unfiltered_client_data = extract_csv("../dataset/Phase#1_data/client.csv")
    filtered_client_data = transform_client_csv(unfiltered_client_data)

    for clid, fname, lname, age, memberyear in filtered_client_data.values:
        try:
            cur.execute("INSERT into client (clid, fname, lname, age, memberyear) VALUES(%s, %s, %s, %s, %s);", (clid, fname, lname, age, memberyear))
        except Exception as e:
            print("An error occurred while inserting into client table: ", e)
            pass


    conn.commit()
    db.disconnect()

def load_room_unavailable_csv():

    db.connect()
    conn = get_connection()
    cur = get_cursor()


    unfiltered_room_unavailable_data = extract_csv("../dataset/Phase#1_data/room_unavailable.csv")
    filtered_room_unavailable_data = transform_room_unavailable_csv(unfiltered_room_unavailable_data)

    for ruid, rid, startdate, enddate in filtered_room_unavailable_data.values:
        try:
            cur.execute("INSERT into roomunavailable1 (ruid, rid, startdate, enddate) VALUES(%s, %s, %s, %s);", (ruid, rid, startdate, enddate))
        except Exception as e:
            print("An error occurred while inserting into roomunavailable table: ", e)
            pass


    conn.commit()
    db.disconnect()

load_room_unavailable_csv()