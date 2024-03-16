import pandas as pd
from database import db, get_connection, get_cursor

def extract_xlsx(path):
    return pd.read_excel(path)

# Transform
def trasnform_chain_data(unfiltered_data):
    unfiltered_data = unfiltered_data.rename(columns ={"id":"chid", "name":"cname", "spring":"springmkup", "summer":"summermkup", "fall":"fallmkup", "winter":"wintermkup"})
    filtered_data = unfiltered_data.dropna()
    return filtered_data 

def trasnform_login_data(unfiltered_data):
    unfiltered_data = unfiltered_data.rename(columns ={"lid":"lid", "employeeid":"eid", "user":"username", "pass":"password"})
    filtered_data = unfiltered_data.dropna()
    return filtered_data 

# Load
def load_chain_xlsx():
    db.connect()
    conn = get_connection()
    cur = get_cursor()

    unfiltered_chain_data = extract_xlsx("./dataset/Phase#1_data/chain.xlsx")
    filtered_chain_data = trasnform_chain_data(unfiltered_chain_data)

    for chid, cname, springmkup, summermkup, fallmkup, wintermkup in filtered_chain_data.values:
        try:
            cur.execute("INSERT into chains (chid, cname, springmkup, summermkup, fallmkup, wintermkup) VALUES (%s, %s, %s, %s, %s, %s);", (chid, cname, springmkup, summermkup, fallmkup, wintermkup ))
            conn.commit()
        except Exception as e:
            print("Inserting error:", e)
            pass
    print("All chain data was inserted")

    
def load_login_xlsx():
    conn = get_connection()
    cur = get_cursor()

    unfiltered__login_data = extract_xlsx("./dataset/Phase#1_data/login.xlsx")
    filtered_login_data = trasnform_login_data(unfiltered__login_data)

    for lid, eid, username, password in filtered_login_data.values:
        try:
            cur.execute("INSERT into login (lid, eid, username, password) VALUES (%s, %s, %s, %s);", (lid, eid, username, password))
            conn.commit()
        except Exception as e:
            print("Inserting error:", e)
            pass
    print("All login data was inserted")
