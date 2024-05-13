import requests

url = "http://127.0.0.1:5000/"

def getIndexTest():
    return requests.get(url)

def getTopThreeTotalRevenue(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "most/revenue", json=info, headers=headers)

def getpercentageByPaymentMethod(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "paymentmethod", json=info, headers=headers)
      
def handlergetTopThreeLeastRooms(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "least/rooms", json=info, headers=headers)

def getTopFiveHotelsMostCapacity(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "most/capacity", json=info, headers=headers)

def getTopTenByHotelReservation(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "most/reservation", json=info, headers=headers)

def getTopThreeMonthByChain(info):
    headers = {'Content-Type': 'application/json'}
    return requests.post(url + "most/profitmonth", json=info, headers=headers)