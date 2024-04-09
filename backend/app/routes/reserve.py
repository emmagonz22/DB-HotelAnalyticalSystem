from __main__ import app
from flask import request
from ..controller.reserve import BaseReserve


@app.route('/reserve', methods=['GET', 'POST'])
def handleReserve():
    if request.method == 'GET':
        return BaseReserve().getAllReserve()
    elif request.method == 'POST':
        return BaseReserve().createReserve(request.json)
    return "Not reachable!"

@app.route('/reserve/<reid>', methods=['GET', 'PUT', 'DELETE'])
def handleReservebyId(reid):
    if request.method == 'GET':
        return BaseReserve().getReservebyId(int(reid))
    elif request.method == 'DELETE':
        return BaseReserve().deleteReservebyId(int(reid))
    elif request.method == 'PUT':
       return BaseReserve().updateReservebyId(request.json)
    return "Not reachable!"
