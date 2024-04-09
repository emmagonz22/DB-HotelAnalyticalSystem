from app.models.client import ClientDAO
from flask import jsonify

class BaseClient:
    def getAllClients(self):
        model = ClientDAO()
        result = model.getAllClients()
        return jsonify(result)

    def getClientbyId(self, clid):
        model = ClientDAO()
        result = model.getClientbyId(clid)
        return jsonify(result)

    def createClient(self, json):
        model = ClientDAO()
        result = model.createClient(json)
        return jsonify(result)

    def deleteClientbyId(self, clid):
        model = ClientDAO()
        result = model.deleteClientbyId(clid)
        if result:
            return jsonify(result), 200 
        return jsonify("Client Not Found"), 404

    def updateClientbyId(self, json):
        model = ClientDAO()
        result = model.updateClientbyId(json)
        if result:
            return jsonify(result), 200 
        return jsonify("Client Not Found"), 404