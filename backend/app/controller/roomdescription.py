from app.models.room_description import RoomDescriptionDAO
from flask import jsonify

class BaseRoomDescription:
    def getAllRoomDescription(self):
        model = RoomDescriptionDAO()
        result = model.getAllRoomDescription()
        return jsonify(result), 200

    def getRoomDescriptionbyId(self, rdid):
        model = RoomDescriptionDAO()
        result = model.getRoomDescriptionbyId(rdid)
        return jsonify(result), 200

    def createRoomDescription(self, json):
        model = RoomDescriptionDAO()
        result = model.createRoomDescription(json)
        return jsonify(result), 200

    def deleteRoomDescriptionbyId(self, rdid):
        model = RoomDescriptionDAO()
        result = model.deleteRoomDescriptionbyId(rdid)
        if result:
            return jsonify(result), 200 
        return jsonify("Room Description Not Found"), 404

    def updateRoomDescriptionbyId(self, json):
        model = RoomDescriptionDAO()
        result = model.updateRoomDescriptionbyId(json)
        if result:
            return jsonify(result), 200 
        return jsonify("Room Description Not Found"), 404