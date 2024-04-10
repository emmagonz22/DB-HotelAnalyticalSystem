from __main__ import app
from flask import request
from ..controller.globals import BaseGlobalStatistic

@app.route('/most/revenue', methods=["GET"])
def getTopThreeTotalRevenue():
      if request.method == 'GET':
        return BaseGlobalStatistic().getTopThreeTotalRevenue()
      return "Not reachable!"

@app.route('/paymentmethod', methods=["GET"])
def ggetpercentageByPaymentMethod():
      if request.method == 'GET':
        return BaseGlobalStatistic().getpercentageByPaymentMethod()
      return "Not reachable!"
      
@app.route('/least/rooms', methods=["GET"])
def handlergetTopThreeLeastRooms():

    if request.method == 'GET':
        return BaseGlobalStatistic().getTopThreeLeastRooms()

    return "Not reachable!"

@app.route('/most/capacity', methods=["GET"])
def getTopFiveHotelsMostCapacity():
    if request.method == "GET":
        return BaseGlobalStatistic().getTopFiveHotelsMostCapacity()

    return "Not reachable!"


@app.route('/most/reservation', methods=["GET"])
def  getTopTenByHotelReservation():
      if request.method == 'GET':
        return BaseGlobalStatistic(). getTopTenByHotelReservation()
      return "Not reachable!"

@app.route('/most/profitmonth', methods=["GET"])
def getTopThreeMonthByChain():
      if request.method == 'GET':
        return BaseGlobalStatistic().getTopThreeMonthByChain()
      return "Not reachable!"
