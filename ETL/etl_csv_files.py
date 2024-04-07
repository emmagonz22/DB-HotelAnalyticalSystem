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
        'lastname' : 'lname',
        'age' : 'age',
        'memberyear' : 'memberyear'
    })
    filtered_data = renamed_data.dropna()
    return filtered_data

def transform_room_unavailable_csv(unfiltered_data):
    renamed_data = unfiltered_data.rename(columns={
        'ruid' : "ruid",
        'rid' : 'rid',
        'start_date' : 'startdate',
        'end_date' : 'enddate'
    })
    filtered_data = renamed_data.dropna()
    return filtered_data

# Load
def load_hotel_csv():
    conn = get_connection()
    cur = get_cursor()


    unfiltered_hotel_data = extract_csv("./dataset/Phase#1_data/hotel.csv")
    filtered_hotel_data = transform_hotel_csv(unfiltered_hotel_data)

    for hid, chid, hname, hcity in filtered_hotel_data.values:
        try:
            cur.execute("INSERT into hotel (hid, chid, hname, hcity) VALUES(%s, %s, %s, %s);", (hid, chid, hname, hcity))
            conn.commit()
        except Exception as e:
            print("An error occurred while inserting into hotel: ", e)
            pass
    print("All hotel data was inserted")




def load_client_csv():

    conn = get_connection()
    cur = get_cursor()

    unfiltered_client_data = extract_csv("./dataset/Phase#1_data/client.csv")
    filtered_client_data = transform_client_csv(unfiltered_client_data)

    for clid, fname, lname, age, memberyear in filtered_client_data.values:
        try:
            cur.execute("INSERT into client (clid, fname, lname, age, memberyear) VALUES(%s, %s, %s, %s, %s);", (clid, fname, lname, age, memberyear))
            conn.commit()
        except Exception as e:
            print("An error occurred while inserting into client table: ", e)
            pass
    print("All client data was inserted")



def load_room_unavailable_csv():

    conn = get_connection()
    cur = get_cursor()


    unfiltered_room_unavailable_data = extract_csv("./dataset/Phase#1_data/roomunavailable.csv")
    filtered_room_unavailable_data = transform_room_unavailable_csv(unfiltered_room_unavailable_data)
    for ruid, rid, startdate, enddate in filtered_room_unavailable_data.values:
        try:
            cur.execute("INSERT into roomunavailable (ruid, rid, startdate, enddate) VALUES(%s, %s, %s, %s);", (int(ruid), int(rid), startdate, enddate))
            conn.commit()
        except Exception as e:
            print("An error occurred while inserting into roomunavailable table: ", e)
            pass
    
    print("All room unavailable data was inserted")

