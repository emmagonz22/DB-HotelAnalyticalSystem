from app.models.client import ClientDAO
from flask import jsonify

class BaseClient:
    def getAllClients(self):
        model = ClientDAO()
        result = model.getAllClients()
        if isinstance(result, list):
            return jsonify(result), 200
        return jsonify(result), 404

    def getClientbyId(self, clid):
        model = ClientDAO()
        result = model.getClientbyId(clid)
        if isinstance(result, dict):
            return jsonify(result), 200
        return jsonify(result), 404

    def createClient(self, json):
        model = ClientDAO()
        result = model.createClient(json)
        if isinstance(result, dict):
            return jsonify(result), 201
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404

    def deleteClientbyId(self, clid):
        model = ClientDAO()
        result = model.deleteClientbyId(clid)
        if result.startswith("Deleted"):
            return jsonify(result), 200 
        return jsonify(result), 404

    def updateClientbyId(self, json):
        model = ClientDAO()
        result = model.updateClientbyId(json)
        if result.startswith("Updated"):
            return jsonify(result), 200
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404