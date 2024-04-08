from app.models.hotel import HotelDAO
from flask import jsonify

class BaseHotel:
    def getAllHotel(self):
        model = HotelDAO()
        result = model.getAllHotel()
        return jsonify(result)
    
    def getHotelbyId(self,hid):
        model=HotelDAO()
        result=model.getHotelbyId(hid)
        return jsonify(result)
    
    def createHotel(self,json):
        model=HotelDAO()
        result=model.createHotel(json)
        return result

    def deleteHotelbyId(self,eid):
        model=HotelDAO()
        result=model.deleteHotelbyId(eid)
        if result:
            return jsonify(result),200
        return jsonify("Hotel Not Found"),404 
    
    def updateHotelbyId(self,json):
        model=HotelDAO()
        result= model.updateHotelbyId(json)
        if result:
            return jsonify(result),200
        return jsonify("Hotel Not Found"),404