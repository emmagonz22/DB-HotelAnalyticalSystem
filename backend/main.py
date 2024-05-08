from app import create_app
from flask import request, jsonify

from app.controller.chains import BaseChains
from app.controller.client import BaseClient
from app.controller.employee import BaseEmployee
from app.controller.globals import BaseGlobalStatistic
from app.controller.hotel import BaseHotel
from app.controller.local import BaseLocalStatistic
from app.controller.login import BaseLogin
from app.controller.reserve import BaseReserve
from app.controller.room import BaseRoom
from app.controller.roomdescription import BaseRoomDescription
from app.controller.roomunavailable import BaseRoomUnavailable


app = create_app()

#import .app.routes
#from app.routes import *

@app.route('/')
def index(): # Temporary index endpoint
    return "<h1>Index page</h1>"

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


@app.route('/most/revenue', methods=["POST"])
def getTopThreeTotalRevenue():
      if request.method == 'POST':
        return BaseGlobalStatistic().getTopThreeTotalRevenue(request.json)
      return "Not reachable!"

@app.route('/paymentmethod', methods=["POST"])
def ggetpercentageByPaymentMethod():
      if request.method == 'POST':
        return BaseGlobalStatistic().getpercentageByPaymentMethod(request.json)
      return "Not reachable!"
      
@app.route('/least/rooms', methods=["POST"])
def handlergetTopThreeLeastRooms():

    if request.method == 'POST':
        return BaseGlobalStatistic().getTopThreeLeastRooms(request.json)

    return "Not reachable!"

@app.route('/most/capacity', methods=["POST"])
def getTopFiveHotelsMostCapacity():
    if request.method == "POST":
        return BaseGlobalStatistic().getTopFiveHotelsMostCapacity(request.json)

    return "Not reachable!"


@app.route('/most/reservation', methods=["POST"])
def  getTopTenByHotelReservation():
      if request.method == 'POST':
        return BaseGlobalStatistic().getTopTenByHotelReservation(request.json)
      return "Not reachable!"

@app.route('/most/profitmonth', methods=["POST"])
def getTopThreeMonthByChain():
      if request.method == 'POST':
        return BaseGlobalStatistic().getTopThreeMonthByChain(request.json)
      return "Not reachable!"


@app.route('/hotel', methods=['GET','POST'])
def getAllHotel():
    if request.method == 'GET':
        return BaseHotel().getAllHotel()
    elif request.method == 'POST':
        return BaseHotel().createHotel(request.json)
    return "Not reachable!"

@app.route('/hotel/<hid>', methods=['GET', 'PUT','DELETE'])
def getHotelbyId(hid):
    if request.method == 'GET':
        return BaseHotel().getHotelbyId(int(hid))
    elif request.method == 'DELETE':
        return BaseHotel().deleteHotelbyId(int(hid))
    elif request.method == 'PUT':
        return BaseHotel().updateHotelbyId(request.json)
    return "Not reachable!"

@app.route('/hotel/<int:hid>/handicaproom', methods=['POST'])
def handlerTopFiveRoomHandicap(hid):

    if request.method == 'POST':
        return BaseLocalStatistic().obtainTopFiveHandicapReserveRoom(hid, request.json)

    return "Not reachable!"

@app.route('/hotel/<int:hid>/leastreserve', methods=['POST'])
def handlerTopThreeLeastTimeUnavailableRoom(hid):
    if request.method == 'POST':
        return BaseLocalStatistic().obtainTopThreeLeastTimeUnavailableRoom(hid, request.json)
    return "Not reachable!"
    
@app.route('/hotel/<int:hid>/mostcreditcard', methods=['POST'])
def handlerTopFiveMostCreditCard(hid):

    if request.method == "POST":
        return BaseLocalStatistic().obtainTopFiveMostCreditCards(hid, request.json)

    return "Not reachable!"


@app.route('/hotel/<int:hid>/highestpaid', methods=['POST'])
def handlerTopThreeHighestPaidRegularEmployee(hid):

    if request.method == "POST":
        return BaseLocalStatistic().obtainTopThreeHighestPaidRegularEmployee(hid, request.json)

    return "Not reachable!"



@app.route('/hotel/<int:hid>/mostdiscount', methods=['POST'])
def handlerTopFiveClientsMostDiscounts(hid):

    if request.method == "POST":
        return BaseLocalStatistic().obtainTopFiveClientsMostDiscounts(hid, request.json)

    return "Not reachable!"


@app.route('/hotel/<int:hid>/roomtype', methods=['POST'])
def handlerTotalReservationRoomType(hid):
    if request.method == "POST":
        return BaseLocalStatistic().obtainTotalReservationRoomType(hid, request.json)

    return "Not reachable!"


@app.route('/hotel/<int:hid>/leastguests', methods=['POST'])
def handlerTopThreeReservedLeastGuestToCapacityRatio(hid):
    if request.method == "POST":
        return BaseLocalStatistic().obtainTopThreeRoomsReservedLeastGuestToCapacityRatio(hid, request.json)

    return "Not reachable!"


@app.route('/login', methods=['GET', 'POST'])
def handleAllLogin():
    if request.method == 'GET':
        return BaseLogin().getAllLogin()
    elif request.method == 'POST':
        return BaseLogin().createLogin(request.json)
    return "Not reachable!"

@app.route('/login/<lid>', methods=['GET', 'PUT', 'DELETE'])
def handleLoginbyId(lid):
    if request.method == 'GET':
        return BaseLogin().getLoginbyId(int(lid))
    elif request.method == 'DELETE':
        return BaseLogin().deleteLoginbyId(int(lid))
    elif request.method == 'PUT':
        return BaseLogin().updateLoginbyId(request.json)
    return "Not reachable!"

@app.route('/auth', methods=["POST"])
def userLogin():    
    if request.method == 'POST':
        data = request.json
        username = data.get('username')
        password = data.get('password')

        all_users = BaseLogin().getAllLogin()
        
        for user, index in enumerate(all_users):
            if user.get('username') == username and user.get('password') == password:
                return jsonify({'status': 'success', 'username' : user.get('username'), 'lid': user.get('lid'), 'eid' : user.get('eid') })
                
        return jsonify({'status': 'Wrong username or password'})
         

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


@app.route('/room', methods=['GET', 'POST'])
def getAllRoom():
    if request.method == 'GET':
        return BaseRoom().getAllRoom()
    elif request.method == 'POST':
        return BaseRoom().createRoom(request.json)
    return "Not reachable!"

@app.route('/room/<rid>', methods=['GET', 'PUT', 'DELETE'])
def getRoombyId(rid):
    if request.method == 'GET':
        return BaseRoom().getRoombyId(int(rid))
    elif request.method == 'DELETE':
        return BaseRoom().deleteRoombyId(int(rid))
    elif request.method == 'PUT':
       return BaseRoom().updateRoombyId(request.json)
    return "Not reachable!"

@app.route('/roomdescription', methods=['GET', 'POST'])
def handleRoomDescription():
    if request.method == 'GET':
        return BaseRoomDescription().getAllRoomDescription()
    elif request.method == 'POST':
        return BaseRoomDescription().createRoomDescription(request.json)
    return "Not reachable!"

@app.route('/roomdescription/<rdid>', methods=['GET', 'PUT', 'DELETE'])
def handleRoomDescriptionbyId(rdid):
    if request.method == 'GET':
        return BaseRoomDescription().getRoomDescriptionbyId(int(rdid))
    elif request.method == 'DELETE':
        return BaseRoomDescription().deleteRoomDescriptionbyId(int(rdid))
    elif request.method == 'PUT':
       return BaseRoomDescription().updateRoomDescriptionbyId(request.json)
    return "Not reachable!"

@app.route('/roomunavailable', methods=['GET', 'POST'])
def getAllRoomUnavailable():
    if request.method == 'GET':
        return BaseRoomUnavailable().getAllRoomUnavailable()
    elif request.method == 'POST':
        return BaseRoomUnavailable().createRoomUnavailable(request.json)
    return "Not reachable!"

@app.route('/roomunavailable/<ruid>', methods=['GET', 'PUT', 'DELETE'])
def getRoomUnavailablebyId(ruid):
    if request.method == 'GET':
        return BaseRoomUnavailable().getRoomUnavailablebyId(int(ruid))
    elif request.method == 'DELETE':
        return BaseRoomUnavailable().deleteRoomUnavailablebyId(int(ruid))
    elif request.method == 'PUT':
       return BaseRoomUnavailable().updateRoomUnavailablebyId(request.json)
    return "Not reachable!"

if __name__ == "__main__":
  
    app.run()