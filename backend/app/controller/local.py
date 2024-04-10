from app.models.local import LocalStatisticsDAO
from flask import jsonify

class BaseLocalStatistic:
    
    def obtainTopFiveHandicapReserveRoom(self, hid ):
        model = LocalStatisticsDAO()
        result = model.handicapRoom(hid)
        return jsonify(result)

    def obtainTopThreeLeastTimeUnavailableRoom(self, hid):
        model = LocalStatisticsDAO()
        result = model.leastReserve(hid)
        return jsonify(result)

    def obtainTopFiveMostCreditCards(self, hid):
        model = LocalStatisticsDAO()
        result = model.mostCreditCard(hid)
        return jsonify(result)

    def obtainTopThreeHighestPaidRegularEmployee(self, hid):
        model = LocalStatisticsDAO()
        result = model.highestPaid(hid)
        return jsonify(result)
    
    def obtainTopFiveClientsMostDiscounts(self, hid):
        model = LocalStatisticsDAO()
        result = model.mostDiscount(hid)
        return jsonify(result)

    def obtainTotalReservationRoomType(self, hid):
        model = LocalStatisticsDAO()
        result = model.roomType(hid)
        return jsonify(result)

    def obtainTopThreeRoomsReservedLeastGuestToCapacityRatio(self, hid):
        model = LocalStatisticsDAO()
        result = model.leastGuests(hid)
        return jsonify(result)