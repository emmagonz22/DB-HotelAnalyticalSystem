from app.models.globals import GlobalStatisticsDAO
from flask import jsonify

class BaseGlobalStatistic:

    def getTopThreeTotalRevenue(self, json):
        model = GlobalStatisticsDAO()
        result = model.getTopThreeTotalRevenue(json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404
    
    def getpercentageByPaymentMethod(self, json):
        model = GlobalStatisticsDAO()
        result = model.getpercentageByPaymentMethod(json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404

    def getTopThreeLeastRooms(self, json):
        model = GlobalStatisticsDAO()
        result = model.getTopThreeLeastRooms(json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404

    def getTopFiveHotelsMostCapacity(self, json):
        model = GlobalStatisticsDAO()
        result = model.getTopFiveHotelsMostCapacity(json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404
    
    def getTopTenByHotelReservation(self, json):
        model = GlobalStatisticsDAO()
        result = model.getTopTenByHotelReservation(json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404

    def getTopThreeMonthByChain(self, json):
        model = GlobalStatisticsDAO()
        result = model.getTopThreeMonthByChain(json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404
