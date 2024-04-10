from app.models.local import LocalStatisticsDAO
from flask import jsonify

class BaseLocalStatistic:
    
    def obtainTopFiveHandicapReserveRoom(self, hid, json):
        model = LocalStatisticsDAO()
        result = model.handicapRoom(hid, json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404


    def obtainTopThreeLeastTimeUnavailableRoom(self, hid, json):
        model = LocalStatisticsDAO()
        result = model.leastReserve(hid, json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404

    def obtainTopFiveMostCreditCards(self, hid, json):
        model = LocalStatisticsDAO()
        result = model.mostCreditCard(hid, json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404

    def obtainTopThreeHighestPaidRegularEmployee(self, hid, json):
        model = LocalStatisticsDAO()
        result = model.highestPaid(hid, json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404
    
    def obtainTopFiveClientsMostDiscounts(self, hid, json):
        model = LocalStatisticsDAO()
        result = model.mostDiscount(hid, json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404

    def obtainTotalReservationRoomType(self, hid, json):
        model = LocalStatisticsDAO()
        result = model.roomType(hid, json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404

    def obtainTopThreeRoomsReservedLeastGuestToCapacityRatio(self, hid, json):
        model = LocalStatisticsDAO()
        result = model.leastGuests(hid, json)
        if (isinstance(result, list)):
            return jsonify(result), 200
        return jsonify(result), 404