from app.models.chains import ChainsDAO
from flask import jsonify

class BaseChains:
    def getAllChains(self):
        model = ChainsDAO()
        result = model.getAllChains()
        if isinstance(result, list):
            return jsonify(result)
        return jsonify(result), 404

    def getChainsbyId(self, chid):
        model = ChainsDAO()
        result = model.getChainsbyId(chid)
        if isinstance(result, dict):
            return jsonify(result), 200
        return jsonify(result), 404

    def createChain(self, json):
        model = ChainsDAO()
        result = model.createChain(json)
        if isinstance(result, dict):
            return jsonify(result), 201
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404

    def deleteChainbyId(self, chid):
        model = ChainsDAO()
        result = model.deleteChainbyId(chid)
        if result.startswith("Deleted"):
            return jsonify(result), 200 
        return jsonify(result), 404

    def updateChainbyId(self, json):
        model = ChainsDAO()
        result = model.updateChainbyId(json)
        if result.startswith("Updated"):
            return jsonify(result), 200
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404