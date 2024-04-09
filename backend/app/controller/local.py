from app.models.local import LocalStatisticsDAO
from flask import jsonify

class BaseLocalStatistic:
    
    def getTopFiveHandicapReserveRoom(self, hid ):
        model = LocalStatisticsDAO()
        result = model.handicapRoom(hid)
        return jsonify(result)

    def getTopThreeLeastTimeUnavailableRoom(self, hid):
        model = LocalStatisticsDAO()
        result = model.leastReserve(hid)
        return jsonify(result)

    def getTopFiveMostCreditCards(self, hid):
        model = LocalStatisticsDAO()
        result = model.mostCreditCard(hid)
        return jsonify(result)

    def getTopThreeHighestPaidRegularEmployee(self, hid):
        model = LocalStatisticsDAO()
        result = model.highestPaid(hid)
        return jsonify(result)
    
    def getTopFiveClientsMostDiscounts(self, hid):
        model = LocalStatisticsDAO()
        result = model.mostDiscount(hid)
        return jsonify(result)

    def getTotalReservationRoomType(self, hid):
        model = LocalStatisticsDAO()
        result = model.roomType(hid)
        return jsonify(result)

    def getTopThreeRoomsReservedLeastGuestToCapacityRatio(self, hid):
        model = LocalStatisticsDAO()
        result = model.leastGuests(hid)
        return jsonify(result)