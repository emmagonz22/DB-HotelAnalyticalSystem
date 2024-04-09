from __main__ import app
from flask import request
from ..controller.roomdescription import BaseRoomDescription


@app.route('/roomdescription', methods=['GET', 'POST'])
def handleRoomDescription():
    if request.method == 'GET':
        return BaseRoomDescription().getAllRoomDescription()
    elif request.method == 'POST':
        return BaseRoomDescription().createRoomDescription(request.json)
    return "Not reachable!"

@app.route('/roomdescription/<rdid>', methods=['GET', 'PUT', 'DELETE'])
def handleRoomDescriptionbyId(rdid):
    if request.method == 'GET':
        return BaseRoomDescription().getRoomDescriptionbyId(int(rdid))
    elif request.method == 'DELETE':
        return BaseRoomDescription().deleteRoomDescriptionbyId(int(rdid))
    elif request.method == 'PUT':
       return BaseRoomDescription().updateRoomDescriptionbyId(request.json)
    return "Not reachable!"
