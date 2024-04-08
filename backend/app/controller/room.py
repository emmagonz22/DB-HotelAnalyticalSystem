from app.models.room import RoomDAO
from flask import jsonify

class BaseRoom:
    def getAllRoom(self):
        model = RoomDAO()
        result = model.getAllRoom()
        return jsonify(result)
    
    def getRoombyId(self, rid):
        model = RoomDAO()
        result = model.getRoombyId(rid)
        return jsonify(result)
    
    def createRoom(self, json):
        model = RoomDAO()
        result = model.createRoom(json)
        return jsonify(result)
    
    def deleteRoombyId(self, rid):
        model = RoomDAO()
        result = model.deleteRoombyId(rid)
        if result:
            return jsonify(result), 200 
        return jsonify("Room Not Found"), 404
    
    def updateRoombyId(self, json):
        model = RoomDAO()
        result = model.updateRoombyId(json)
        if result:
            return jsonify(result), 200 
        return jsonify("Room Not Found"), 404

