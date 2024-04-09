from __main__ import app
from flask import request
from ..controller.roomunavailable import BaseRoomUnavailable


@app.route('/roomunavailable', methods=['GET', 'POST'])
def getAllRoomUnavailable():
    if request.method == 'GET':
        return BaseRoomUnavailable().getAllRoomUnavailable()
    elif request.method == 'POST':
        return BaseRoomUnavailable().createRoomUnavailable(request.json)
    return "Not reachable!"

@app.route('/roomunavailable/<ruid>', methods=['GET', 'PUT', 'DELETE'])
def getRoomUnavailablebyId(ruid):
    if request.method == 'GET':
        return BaseRoomUnavailable().getRoomUnavailablebyId(int(ruid))
    elif request.method == 'DELETE':
        return BaseRoomUnavailable().deleteRoomUnavailablebyId(int(ruid))
    elif request.method == 'PUT':
       return BaseRoomUnavailable().updateRoomUnavailablebyId(request.json)
    return "Not reachable!"