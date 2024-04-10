from app.models.globals import GlobalStatisticsDAO
from flask import jsonify

class BaseGlobalStatistic:

    def getTopThreeTotalRevenue(self):
        model = GlobalStatisticsDAO()
        result = model.getTopThreeTotalRevenue()
        return jsonify(result)
    
    def getpercentageByPaymentMethod(self):
        model = GlobalStatisticsDAO()
        result = model.getpercentageByPaymentMethod()
        return jsonify(result)

    def getTopThreeLeastRooms(self):
        model = GlobalStatisticsDAO()
        result = model.getTopThreeLeastRooms()
        return jsonify(result)

    def getTopFiveHotelsMostCapacity(self):
        model = GlobalStatisticsDAO()
        result = model.getTopFiveHotelsMostCapacity()
        return jsonify(result)
    
    def getTopTenByHotelReservation(self):
        model = GlobalStatisticsDAO()
        result = model.getTopTenByHotelReservation()
        return jsonify(result)

    def getTopThreeMonthByChain(self):
        model = GlobalStatisticsDAO()
        result = model.getTopThreeMonthByChain()
        return jsonify(result)
