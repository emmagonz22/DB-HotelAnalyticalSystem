from app.models.hotel import HotelDAO
from flask import jsonify

class BaseHotel:
    def getAllHotel(self):
        model = HotelDAO()
        result = model.getAllHotel()
        return jsonify(result)