import requests

url = "https://db-hotel-analytics-systems-6a60248fdbac.herokuapp.com/"

def getIndexTest():
    return requests.get(url)

def getTopThreeTotalRevenue(json):
    return requests.post(url + "most/revenue", json)

def getpercentageByPaymentMethod(json):
    return requests.post(url + "paymentmethod", json)
      
def handlergetTopThreeLeastRooms(json):
    return requests.post(url + "least/rooms", json)

def getTopFiveHotelsMostCapacity(json):
    return requests.post(url + "most/capacity", json)

def getTopTenByHotelReservation(json):
    return requests.post(url + "most/reservation", json)

def getTopThreeMonthByChain(json):
    return requests.post(url + "most/profitmonth", json)