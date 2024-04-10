from __main__ import app
from flask import request
from ..controller.hotel import BaseHotel
from ..controller.local import BaseLocalStatistic

@app.route('/hotel', methods=['GET','POST'])
def getAllHotel():
    if request.method == 'GET':
        return BaseHotel().getAllHotel()
    elif request.method == 'POST':
        return BaseHotel().createHotel(request.json)
    return "Not reachable!"

@app.route('/hotel/<hid>', methods=['GET', 'PUT','DELETE'])
def getHotelbyId(hid):
    if request.method == 'GET':
        return BaseHotel().getHotelbyId(int(hid))
    elif request.method == 'DELETE':
        return BaseHotel().deleteHotelbyId(int(hid))
    elif request.method == 'PUT':
        return BaseHotel().updateHotelbyId(request.json)
    return "Not reachable!"

@app.route('/hotel/<hid>/handicaproom', methods=["GET",'POST'])
def handlerTopFiveRoomHandicap(hid):

    if request.method == 'POST':
        return BaseLocalStatistic().obtainTopFiveHandicapReserveRoom(hid)

    return "Not reachable!"

@app.route('/hotel/<hid>/leastreserve', methods=["GET",'POST'])
def handlerTopThreeLeastTimeUnavailableRoom(hid):
    if request.method == 'POST':
        return BaseLocalStatistic().obtainTopThreeLeastTimeUnavailableRoom(hid)
    return "Not reachable!"
    
@app.route('/hotel/<hid>/mostcreditcard', methods=["GET",'POST'])
def handlerTopFiveMostCreditCard(hid):

    if request.method == "POST":
        return BaseLocalStatistic().obtainTopFiveMostCreditCards(hid)

    return "Not reachable!"


@app.route('/hotel/<hid>/highestpaid', methods=["GET",'POST'])
def handlerTopThreeHighestPaidRegularEmployee(hid):

    if request.method == "POST":
        return BaseLocalStatistic().obtainTopThreeHighestPaidRegularEmployee(hid)

    return "Not reachable!"



@app.route('/hotel/<hid>/mostdiscount', methods=["GET",'POST'])
def handlerTopFiveClientsMostDiscounts(hid):

    if request.method == "POST":
        return BaseLocalStatistic().obtainTopFiveClientsMostDiscounts(hid)

    return "Not reachable!"


@app.route('/hotel/<hid>/roomtype', methods=["GET",'POST'])
def handlerTotalReservationRoomType(hid):
    if request.method == "POST":
        return BaseLocalStatistic().obtainTotalReservationRoomType(hid)

    return "Not reachable!"


@app.route('/hotel/<hid>/leastguests', methods=["GET",'POST'])
def handlerTopThreeReservedLeastGuestToCapacityRatio(hid):
    if request.method == "POST":
        return BaseLocalStatistic().obtainTopThreeRoomsReservedLeastGuestToCapacityRatio(hid)

    return "Not reachable!"