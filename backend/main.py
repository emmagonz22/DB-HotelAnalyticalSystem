from app import create_app
from flask import request
from app.controller.chains import BaseChains



app = create_app()

#import .app.routes
from app.routes import *

@app.route('/')
def index(): # Temporary index endpoint
    return "<h1>Index page</h1>"

@app.route('/chains', methods=['GET', 'POST'])
def getAllChains():
    if request.method == 'GET':
        return BaseChains().getAllChains()
    elif request.method == 'POST':
        return BaseChains().createChain(request.json)
    return "Not reachable!"

@app.route('/chains/<chid>', methods=['GET', 'PUT'])
def getChainsbyId(chid):
    if request.method == 'GET':
        return BaseChains().getChainsbyId(int(chid))
    return "Not reachable!"

'''
@app.route('/employee', methods=['GET', 'POST'])
def getAllEmployee():
    if request.method == 'GET':
        return BaseEmployee().getAllEmployee()
    elif request.method == 'POST':
        return BaseEmployee().createEmployee(request.json)
    return "Not reachable!"

@app.route('/employee/<eid>', methods=['GET', 'PUT', 'DELETE'])
def getEmployeebyId(eid):
    if request.method == 'GET':
        return BaseEmployee().getEmployeebyId(int(eid))
    elif request.method == 'DELETE':
        return BaseEmployee().deleteEmployeebyId(int(eid))
    elif request.method == 'PUT':
       return BaseEmployee().updateEmployeebyId(request.json)
    return "Not reachable!"
'''
if __name__ == "__main__":
  
    app.run()