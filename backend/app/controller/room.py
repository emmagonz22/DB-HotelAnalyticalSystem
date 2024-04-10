from app.models.room import RoomDAO
from flask import jsonify

class BaseRoom:
    def getAllRoom(self):
        model = RoomDAO()
        result = model.getAllRoom()
        if isinstance(result, list):
            return jsonify(result), 200
        return jsonify(result), 404
    
    def getRoombyId(self, rid):
        model = RoomDAO()
        result = model.getRoombyId(rid)
        if isinstance(result, dict):
            return jsonify(result), 200
        return jsonify(result), 404
    
    def createRoom(self, json):
        model = RoomDAO()
        result = model.createRoom(json)
        if isinstance(result, dict):
            return jsonify(result), 201
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404
    
    def deleteRoombyId(self, rid):
        model = RoomDAO()
        result = model.deleteRoombyId(rid)
        if result.startswith("Deleted"):
            return jsonify(result), 200 
        return jsonify(result), 404
    
    def updateRoombyId(self, json):
        model = RoomDAO()
        result = model.updateRoombyId(json)
        if result.startswith("Updated"):
            return jsonify(result), 200
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404

