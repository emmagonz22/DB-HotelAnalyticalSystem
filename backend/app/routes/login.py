
from __main__ import app
from flask import request
from ..controller.login import BaseLogin


@app.route('/login', methods=['GET', 'POST'])
def handleAllLogin():
    if request.method == 'GET':
        return BaseLogin().getAllLogin()
    elif request.method == 'POST':
        return BaseLogin().createLogin(request.json)
    return "Not reachable!"

@app.route('/login/<lid>', methods=['GET', 'PUT', 'DELETE'])
def handleLoginbyId(eid):
    if request.method == 'GET':
        return BaseLogin().getLoginbyId(int(lid))
    elif request.method == 'DELETE':
        return BaseLogin().deleteLoginbyId(int(lid))
    elif request.method == 'PUT':
        return BaseLogin().updateLoginbyId(request.json)
    return "Not reachable!"

