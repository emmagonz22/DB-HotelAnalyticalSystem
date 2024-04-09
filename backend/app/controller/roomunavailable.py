from app.models.roomunavailable import RoomUnavailableDAO
from flask import jsonify

class BaseRoomUnavailable:
    def getAllRoomUnavailable(self):
        model = RoomUnavailableDAO()
        result = model.getAllRoomUnavailable()
        return jsonify(result)
    
    def getRoomUnavailablebyId(self, eid):
        model = RoomUnavailableDAO()
        result = model.getRoomUnavailablebyId(eid)
        return jsonify(result)
    
    def createRoomUnavailable(self, json):
        model = RoomUnavailableDAO()
        result = model.createRoomUnavailable(json)
        return jsonify(result)
    
    def deleteRoomUnavailablebyId(self, eid):
        model = RoomUnavailableDAO()
        result = model.deleteRoomUnavailablebyId(eid)
        if result:
            return jsonify(result), 200 
        return jsonify("RoomUnavailable Not Found"), 404
    
    def updateRoomUnavailablebyId(self, json):
        model = RoomUnavailableDAO()
        result = model.updateRoomUnavailablebyId(json)
        if result:
            return jsonify(result), 200 
        return jsonify("RoomUnavailable Not Found"), 404

