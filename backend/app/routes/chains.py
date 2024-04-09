from __main__ import app
from flask import request
from ..controller.chains import BaseChains


@app.route('/chains', methods=['GET', 'POST'])
def handleChains():
    if request.method == 'GET':
        return BaseChains().getAllChains()
    elif request.method == 'POST':
        return BaseChains().createChain(request.json)
    return "Not reachable!"

@app.route('/chains/<chid>', methods=['GET', 'PUT', 'DELETE'])
def handleChainsbyId(chid):
    if request.method == 'GET':
        return BaseChains().getChainsbyId(int(chid))
    elif request.method == 'DELETE':
        return BaseChains().deleteChainbyId(int(chid))
    elif request.method == 'PUT':
       return BaseChains().updateChainbyId(request.json)
    return "Not reachable!"
