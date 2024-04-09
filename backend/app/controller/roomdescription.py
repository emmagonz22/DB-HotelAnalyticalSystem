from app.models.room_description import RoomDescriptionDAO
from flask import jsonify

class BaseRoomDescription:
    def getAllRoomDescription(self):
        model = RoomDescriptionDAO()
        result = model.getAllRoomDescription()
        if isinstance(result, dict):
            return jsonify(result), 200
        return jsonify(result), 404

    def getRoomDescriptionbyId(self, rdid):
        model = RoomDescriptionDAO()
        result = model.getRoomDescriptionbyId(rdid)
        if isinstance(result, dict):
            return jsonify(result), 200
        return jsonify(result), 404

    def createRoomDescription(self, json):
        model = RoomDescriptionDAO()
        result = model.createRoomDescription(json)
        if isinstance(result, dict):
            return jsonify(result), 201
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404
    

    def deleteRoomDescriptionbyId(self, rdid):
        model = RoomDescriptionDAO()
        result = model.deleteRoomDescriptionbyId(rdid)
        if result.startswith("Deleted"):
            return jsonify(result), 200 
        return jsonify(result), 404

    def updateRoomDescriptionbyId(self, json):
        model = RoomDescriptionDAO()
        result = model.updateRoomDescriptionbyId(json)
        if result.startswith("Updated"):
            return jsonify(result), 200
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404