from app.models.login import LoginDAO
from flask import jsonify

class BaseLogin:
    def getAllLogin(self):
        model = LoginDAO()
        result = model.getAllLogin()
        if isinstance(result, list):
            return jsonify(result), 200
        return jsonify(result), 404
        

    def getLoginbyId(self, lid):
        model = LoginDAO()
        result = model.getLoginbyId(lid)
        if isinstance(result, dict):
            return jsonify(result), 200
        return jsonify(result), 404
        

    def createLogin(self, json):
        model = LoginDAO()
        result = model.createLogin(json)
        if isinstance(result, dict):
            return jsonify(result), 201
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404

    def updateLoginbyId(self, json):
        model = LoginDAO()
        result = model.updateLoginbyId(json)
        if result.startswith("Updated"):
            return jsonify(result), 200 
        return jsonify(result), 404

    def deleteLoginbyId(self,lid):
        model = LoginDAO()
        result = model.deleteLoginbyId(lid)
        if result.startswith("Deleted"):
            return jsonify(result), 200
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404

    def verifyLogin(self, username, password):
        model = LoginDAO()
        all_users = model.getAllLogin()
      
        for index, user in enumerate(all_users):
            #print(user)
            if user.get('username') == username and user.get('password') == password:
                return user.get('eid')
        
        return None 
