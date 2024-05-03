import requests

url = "https://db-hotel-analytics-systems-6a60248fdbac.herokuapp.com/"

def TopFiveRoomHandicap(hid, json):
    return requests.post(url+"hotel/{hid}/handicaproom", json).content

def TopThreeLeastTimeUnavailableRoom(hid, json):
    return requests.post(url+"hotel/{hid}/leastreserve",json).content
    
def TopFiveMostCreditCard(hid, json):
    return requests.post(url+"hotel/{hid}/mostcreditcard",json).content

def TopThreeHighestPaidRegularEmployee(hid, json):
    return requests.post(url+"hotel/{hid}/highestpaid",json).content

def TopFiveClientsMostDiscounts(hid, json):
    return requests.post(url+"hotel/{hid}/mostdiscount",json).content

def TotalReservationRoomType(hid, json):
    return requests.post(url+"hotel/{hid}/roomtype",json).content

def TopThreeReservedLeastGuestToCapacityRatio(hid, json):
    return requests.post(url+"hotel/{hid}/leastguests",json).content