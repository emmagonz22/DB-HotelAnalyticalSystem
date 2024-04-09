from app.models.login import LoginDAO
from flask import jsonify

class BaseLogin:
    def getAllLogin(self):
        model = LoginDAO()
        return jsonify(model.getAllLogin())
        

    def getLoginbyId(self, lid):
        model = LoginDAO()
        return jsonify(model.getLoginbyId(lid))
        

    def createLogin(self, json):
        model = LoginDAO()
        result = model.createLogin(json)
        return jsonify(result)

    def updateLoginbyId(self, json):
        model = LoginDAO()
        result = model.updateLoginbyId(json)
        if result:
            return jsonify(result), 200
        return jsonify("Login not found"), 404

    def deleteLoginbyId(self,lid):
        model = LoginDAO()
        result = model.deleteLoginbyId(lid)
        if result:
            return jsonify(result), 200
        return jsonify("Login not found"), 404
