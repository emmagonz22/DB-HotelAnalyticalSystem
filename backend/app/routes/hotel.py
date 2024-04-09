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

@app.route('/hotel/<hid>/handicaproom', methods=["GET"])
def handlerTopFiveRoomHandicap(hid):

    if request.method == 'GET':
        return BaseLocalStatistic().getTopFiveHandicapReserveRoom(hid)

    return "Not reachable!"

@app.route('/hotel/<hid>/leastreserve', methods=["GET"])
def handlerTopThreeLeastTimeUnavailableRoom(hid):

    if request.method == 'GET':
        return BaseLocalStatistic().getTopThreeLeastTimeUnavailableRoom(hid)

    return "Not reachable!"
@app.route('/hotel/<hid>/mostcreditcard', methods=["GET"])
def handlerTopFiveMostCreditCard(hid):

    if request.method == "GET":
        return BaseLocalStatistic().getTopFiveMostCreditCards(hid)

    return "Not reachable!"


@app.route('/hotel/<hid>/highestpaid', methods=["GET"])
def handlerTopThreeHighestPaidRegularEmployee(hid):

    if request.method == "GET":
        return BaseLocalStatistic().getTopThreeHighestPaidRegularEmployee(hid)

    return "Not reachable!"