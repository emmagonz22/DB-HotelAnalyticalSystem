from app.models.reserve import ReserveDAO
from flask import jsonify

class BaseReserve:
    def getAllReserve(self):
        model = ReserveDAO()
        result = model.getAllReserve()
        if isinstance(result, list):
            return jsonify(result), 200
        return jsonify(result), 404

    def getReservebyId(self, reid):
        model = ReserveDAO()
        result = model.getReservebyId(reid)
        if isinstance(result, dict):
            return jsonify(result), 200
        return jsonify(result), 404

    def createReserve(self, json):
        model = ReserveDAO()
        result = model.createReserve(json)
        if isinstance(result, dict):
            return jsonify(result), 201
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404

    def deleteReservebyId(self, reid):
        model = ReserveDAO()
        result = model.deleteReservebyId(reid)
        if result.startswith("Deleted"):
            return jsonify(result), 200 
        return jsonify(result), 404

    def updateReservebyId(self, json):
        model = ReserveDAO()
        result = model.updateReservebyId(json)
        if result.startswith("Updated"):
            return jsonify(result), 200
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404