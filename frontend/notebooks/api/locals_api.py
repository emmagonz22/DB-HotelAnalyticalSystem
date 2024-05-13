import requests

url = "http://127.0.0.1:5000/"

def TopFiveRoomHandicap(hid, info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url+f"hotel/{hid}/handicaproom", json =info, headers=headers)

def TopThreeLeastTimeUnavailableRoom(hid, info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url+f"hotel/{hid}/leastreserve",json =info, headers=headers)
    
def TopFiveMostCreditCard(hid, info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url+f"hotel/{hid}/mostcreditcard",json =info, headers=headers)

def TopThreeHighestPaidRegularEmployee(hid, info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url+f"hotel/{hid}/highestpaid",json =info, headers=headers)

def TopFiveClientsMostDiscounts(hid, info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url+f"hotel/{hid}/mostdiscount",json =info, headers=headers)

def TotalReservationRoomType(hid, info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url+f"hotel/{hid}/roomtype",json =info, headers=headers)

def TopThreeReservedLeastGuestToCapacityRatio(hid, info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url+f"hotel/{hid}/leastguests", json =info)