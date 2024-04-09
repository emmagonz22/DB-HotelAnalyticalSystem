from __main__ import app
from flask import request
from ..controller.client import BaseClient


@app.route('/client', methods=['GET', 'POST'])
def handleClient():
    if request.method == 'GET':
        return BaseClient().getAllClients()
    elif request.method == 'POST':
        return BaseClient().createClient(request.json)
    return "Not reachable!"

@app.route('/client/<clid>', methods=['GET', 'PUT', 'DELETE'])
def handleClientbyId(clid):
    if request.method == 'GET':
        return BaseClient().getClientbyId(int(clid))
    elif request.method == 'DELETE':
        return BaseClient().deleteClientbyId(int(clid))
    elif request.method == 'PUT':
       return BaseClient().updateClientbyId(request.json)
    return "Not reachable!"
