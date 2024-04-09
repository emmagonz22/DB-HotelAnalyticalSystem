from __main__ import app
from flask import request
from ..controller.room import BaseRoom


@app.route('/room', methods=['GET', 'POST'])
def getAllRoom():
    if request.method == 'GET':
        return BaseRoom().getAllRoom()
    elif request.method == 'POST':
        return BaseRoom().createRoom(request.json)
    return "Not reachable!"

@app.route('/room/<rid>', methods=['GET', 'PUT', 'DELETE'])
def getRoombyId(rid):
    if request.method == 'GET':
        return BaseRoom().getRoombyId(int(rid))
    elif request.method == 'DELETE':
        return BaseRoom().deleteRoombyId(int(rid))
    elif request.method == 'PUT':
       return BaseRoom().updateRoombyId(request.json)
    return "Not reachable!"