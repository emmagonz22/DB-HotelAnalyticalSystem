import pandas as pd
from database import db, get_connection, get_cursor


# Extract

def extract_json(path):
    return pd.read_json(path)

# Transform

def transform_employee_data(unfiltered_data):
    renamed_data = unfiltered_data.rename(columns={'employeeid': 'eid', 
                                                    'hotelid': 'hid', 
                                                    'firstname': 'fname', 
                                                    'lastname': 'lname'})
    filtered_data = renamed_data.dropna()

    return filtered_data

def transform_roomdetails_data(unfiltered_data):
    renamed_data = unfiltered_data.rename(columns={'detailid': 'rdid', 
                                                    'name': 'rname', 
                                                    'type': 'rtype', 
                                                    'handicap': 'ishandicap'})
    filtered_data = renamed_data.dropna()
    return filtered_data

# Load

def load_employee_json():
    conn = get_connection()
    cur = get_cursor()

    unfiltered_employee_data = extract_json(r"./dataset/Phase#1_data/employee.json")
    filtered_employee_data = transform_employee_data(unfiltered_employee_data)

    for eid, hid, fname, lname, age, salary, position in filtered_employee_data.values:
        try:
            cur.execute("INSERT into employee (eid, hid, fname, lname, age, salary, position) VALUES(%s, %s, %s, %s, %s, %s, %s);", 
                        (eid, hid, fname, lname, age, salary, position))
            conn.commit()
        except Exception as e:
            print("An error occurred while inserting into employee: ", e)
            pass
    print("All employee data was inserted")


def load_roomdetails_json():
    conn = get_connection()
    cur = get_cursor()

    unfiltered_roomdetails_data = extract_json(r"./dataset/Phase#1_data/roomdetails.json")
    filtered_roomdetails_data = transform_roomdetails_data(unfiltered_roomdetails_data)

    for rdid, rname, rtype, capacity, ishandicap in filtered_roomdetails_data.values:
        try:
            cur.execute("INSERT into roomdescription (rdid, rname, rtype, capacity, ishandicap) VALUES(%s, %s, %s, %s, %s);", 
                        (rdid, rname, rtype, capacity, bool(ishandicap)))
            conn.commit()
        except Exception as e:
            print("An error occurred while inserting into employee: ", e)
            pass
    print("All room details data was inserted")

