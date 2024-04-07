from app import create_app
from flask import request
from app.controller.chains import BaseChains
from app.controller.hotel import BaseHotel


app = create_app()

@app.route('/')
def index(): # Temporary index endpoint
    return "<h1>Index page</h1>"

@app.route('/chains', methods=['GET'])
def getAllChains():
    if request.method == 'GET':
        return BaseChains().getAllChains()
    return "Not reachable!"

@app.route('/hotel', methods=['GET'])
def getAllHotel():
    if request.method == 'GET':
        return BaseHotel().getAllHotel()
    return "Not reachable!"

if __name__ == "__main__":
  
    app.run()