from app.models.employee import EmployeeDAO
from flask import jsonify

class BaseEmployee:
    def getAllEmployee(self):
        model = EmployeeDAO()
        result = model.getAllEmployee()
        if isinstance(result, list):
            return jsonify(result), 200
        return jsonify(result), 404
    
    def getEmployeebyId(self, eid):
        model = EmployeeDAO()
        result = model.getEmployeebyId(eid)
        if isinstance(result, dict):
            return jsonify(result), 200
        return jsonify(result), 404
    
    def createEmployee(self, json):
        model = EmployeeDAO()
        result = model.createEmployee(json)
        if isinstance(result, dict):
            return jsonify(result), 201
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404
    
    def deleteEmployeebyId(self, eid):
        model = EmployeeDAO()
        result = model.deleteEmployeebyId(eid)
        if result.startswith("Deleted"):
            return jsonify(result), 200 
        return jsonify(result), 404
    
    def updateEmployeebyId(self, json):
        model = EmployeeDAO()
        result = model.updateEmployeebyId(json)
        if result.startswith("Updated"):
            return jsonify(result), 200
        elif result.startswith("Invalid"):
            return jsonify(result), 400
        return jsonify(result), 404

