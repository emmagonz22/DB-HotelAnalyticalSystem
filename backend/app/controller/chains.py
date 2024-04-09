from app.models.chains import ChainsDAO
from flask import jsonify

class BaseChains:
    def getAllChains(self):
        model = ChainsDAO()
        result = model.getAllChains()
        return jsonify(result)

    def getChainsbyId(self, chid):
        model = ChainsDAO()
        result = model.getChainsbyId(chid)
        return jsonify(result)

    def createChain(self, json):
        model = ChainsDAO()
        result = model.createChain(json)
        return jsonify(result)

    def deleteChainbyId(self, chid):
        model = ChainsDAO()
        result = model.deleteChainbyId(chid)
        if result:
            return jsonify(result), 200 
        return jsonify("Chain Not Found"), 404

    def updateChainbyId(self, json):
        model = ChainsDAO()
        result = model.updateChainbyId(json)
        if result:
            return jsonify(result), 200 
        return jsonify("Chain Not Found"), 404