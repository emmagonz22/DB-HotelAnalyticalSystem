from __main__ import app
from flask import request
from ..controller.hotel import BaseHotel

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