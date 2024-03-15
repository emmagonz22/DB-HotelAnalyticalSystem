import pandas as pd

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
def load_xlsx():

    unfiltered_chain_data = extract_xlsx("../dataset/Phase#1_data/chain.xlsx")
    # unfiltered__login_data = extract_xlsx("./dataset/Phase#1_data/login.xlsx")
    filtered_chain_data = trasnform_chain_data(unfiltered_chain_data)
    # filtered_login_data = trasnform_login_data(unfiltered__login_data)
    
