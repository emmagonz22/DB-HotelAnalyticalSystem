from app.models.roomunavailable import RoomUnavailableDAO
from flask import jsonify

class BaseRoomUnavailable:
    def getAllRoomUnavailable(self):
        model = RoomUnavailableDAO()
        result = model.getAllRoomUnavailable()
        if isinstance(result, list):
            return jsonify(result), 200
        return jsonify(result), 404
    
    def getRoomUnavailablebyId(self, eid):
        model = RoomUnavailableDAO()
        result = model.getRoomUnavailablebyId(eid)
        if isinstance(result, dict):
            return jsonify(result), 200
        return jsonify(result), 404
    
    def createRoomUnavailable(self, json):
        model = RoomUnavailableDAO()
        result = model.createRoomUnavailable(json)
        if isinstance(result, dict):
            return jsonify(result), 201
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404
    
    def deleteRoomUnavailablebyId(self, eid):
        model = RoomUnavailableDAO()
        result = model.deleteRoomUnavailablebyId(eid)
        if result.startswith("Deleted"):
            return jsonify(result), 200 
        return jsonify(result), 404
    
    def updateRoomUnavailablebyId(self, json):
        model = RoomUnavailableDAO()
        result = model.updateRoomUnavailablebyId(json)
        if result.startswith("Updated"):
            return jsonify(result), 200
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404

