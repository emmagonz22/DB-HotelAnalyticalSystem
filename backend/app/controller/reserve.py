from app.models.reserve import ReserveDAO
from flask import jsonify

class BaseReserve:
    def getAllReserve(self):
        model = ReserveDAO()
        result = model.getAllReserve()
        return jsonify(result), 200

    def getReservebyId(self, reid):
        model = ReserveDAO()
        result = model.getReservebyId(reid)
        return jsonify(result), 200

    def createReserve(self, json):
        model = ReserveDAO()
        result = model.createReserve(json)
        return jsonify(result), 200

    def deleteReservebyId(self, reid):
        model = ReserveDAO()
        result = model.deleteReservebyId(reid)
        if result:
            return jsonify(result), 200 
        return jsonify("Reserve Not Found"), 404

    def updateReservebyId(self, json):
        model = ReserveDAO()
        result = model.updateReservebyId(json)
        if result:
            return jsonify(result), 200 
        return jsonify("Reserve Not Found"), 404