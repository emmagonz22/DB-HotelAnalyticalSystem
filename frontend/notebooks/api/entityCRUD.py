import requests

url = "https://db-hotel-analytics-systems-6a60248fdbac.herokuapp.com/"


# Chain
def createChain(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "chains", json=info, headers=headers)

def updateChain(info, id):
    headers = {'Content-Type': 'application/json'}
    return requests.put(url + f"chains/{id}", json=info, headers=headers)

def deleteChain(id):
    headers = {'Content-Type': 'application/json'}
    return requests.delete(url + f"chains/{id}", headers=headers)


# Hotel
def createHotel(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "hotel", json=info, headers=headers)

def updateHotel(info, id):
    headers = {'Content-Type': 'application/json'}
    return requests.put(url + f"hotel/{id}", json=info, headers=headers)

def deleteHotel(id):
    headers = {'Content-Type': 'application/json'}
    return requests.delete(url + f"hotel/{id}", headers=headers)


# Employee
def createEmployee(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "employee", json=info, headers=headers)

def updateEmployee(info, id):
    headers = {'Content-Type': 'application/json'}
    return requests.put(url + f"employee/{id}", json=info, headers=headers)

def deleteEmployee(id):
    headers = {'Content-Type': 'application/json'}
    return requests.delete(url + f"employee/{id}", headers=headers)