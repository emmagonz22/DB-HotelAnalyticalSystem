from app.models.employee import EmployeeDAO
from flask import jsonify

class BaseEmployee:
    def getAllEmployee(self):
        model = EmployeeDAO()
        result = model.getAllEmployee()
        return jsonify(result)
    
    def getEmployeebyId(self, eid):
        model = EmployeeDAO()
        result = model.getEmployeebyId(eid)
        return jsonify(result)
    
    def createEmployee(self, json):
        model = EmployeeDAO()
        result = model.createEmployee(json)
        return jsonify(result)
    
    def deleteEmployeebyId(self, eid):
        model = EmployeeDAO()
        result = model.deleteEmployeebyId(eid)
        if result:
            return jsonify(result), 200 
        return jsonify("Employee Not Found"), 404
    
    def updateEmployeebyId(self, json):
        model = EmployeeDAO()
        result = model.updateEmployeebyId(json)
        if result:
            return jsonify(result), 200 
        return jsonify("Employee Not Found"), 404

