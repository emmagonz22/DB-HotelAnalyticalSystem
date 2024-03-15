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
