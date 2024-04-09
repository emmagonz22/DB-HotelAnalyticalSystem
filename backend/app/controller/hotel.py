from app.models.hotel import HotelDAO
from flask import jsonify

class BaseHotel:
    def getAllHotel(self):
        model = HotelDAO()
        result = model.getAllHotel()
        if isinstance(result, dict):
            return jsonify(result), 200
        return jsonify(result), 404
    
    def getHotelbyId(self,hid):
        model=HotelDAO()
        result=model.getHotelbyId(hid)
        if isinstance(result, dict):
            return jsonify(result), 200
        return jsonify(result), 404
    
    def createHotel(self,json):
        model=HotelDAO()
        result=model.createHotel(json)
        if isinstance(result, dict):
            return jsonify(result), 201
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404

    def deleteHotelbyId(self,eid):
        model=HotelDAO()
        result=model.deleteHotelbyId(eid)
        if result.startswith("Deleted"):
            return jsonify(result), 200 
        return jsonify(result), 404
    
    def updateHotelbyId(self,json):
        model=HotelDAO()
        result= model.updateHotelbyId(json)
        if result.startswith("Updated"):
            return jsonify(result), 200
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404