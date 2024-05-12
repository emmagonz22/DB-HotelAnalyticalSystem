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


# Login
def createLogin(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "login", json=info, headers=headers)

def updateLogin(info, id):
    headers = {'Content-Type': 'application/json'}
    return requests.put(url + f"login/{id}", json=info, headers=headers)

def deleteLogin(id):
    headers = {'Content-Type': 'application/json'}
    return requests.delete(url + f"login/{id}", headers=headers)

def retrieveLogin(id):
    headers = {'Content-Type': 'application/json'}
    data = requests.get(url + f"login", headers=headers)
    for row in data:
        if row["eid"] == id:
            return row
    return ""


# Room
def createRoom(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "room", json=info, headers=headers)

def updateRoom(info, id):
    headers = {'Content-Type': 'application/json'}
    return requests.put(url + f"room/{id}", json=info, headers=headers)

def deleteRoom(id):
    headers = {'Content-Type': 'application/json'}
    return requests.delete(url + f"room/{id}", headers=headers)


# Client
def createClient(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "client", json=info, headers=headers)

def updateClient(info, id):
    headers = {'Content-Type': 'application/json'}
    return requests.put(url + f"client/{id}", json=info, headers=headers)

def deleteClient(id):
    headers = {'Content-Type': 'application/json'}
    return requests.delete(url + f"client/{id}", headers=headers)


# Reserve
def createReserve(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "reserve", json=info, headers=headers)

def updateReserve(info, id):
    headers = {'Content-Type': 'application/json'}
    return requests.put(url + f"reserve/{id}", json=info, headers=headers)

def deleteReserve(id):
    headers = {'Content-Type': 'application/json'}
    return requests.delete(url + f"reserve/{id}", headers=headers)


# Room Description
def createRoomDescription(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "roomdescription", json=info, headers=headers)

def updateRoomDescription(info, id):
    headers = {'Content-Type': 'application/json'}
    return requests.put(url + f"roomdescription/{id}", json=info, headers=headers)

def deleteRoomDescription(id):
    headers = {'Content-Type': 'application/json'}
    return requests.delete(url + f"roomdescription/{id}", headers=headers)


# Room Unavailable
def createRoomUnavailable(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "roomunavailable", json=info, headers=headers)

def updateRoomUnavailable(info, id):
    headers = {'Content-Type': 'application/json'}
    return requests.put(url + f"roomunavailable/{id}", json=info, headers=headers)

def deleteRoomUnavailable(id):
    headers = {'Content-Type': 'application/json'}
    return requests.delete(url + f"roomunavailable/{id}", headers=headers)