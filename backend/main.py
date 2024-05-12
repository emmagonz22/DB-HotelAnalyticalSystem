from app import create_app
from flask import request, jsonify, Flask, redirect

from flask_login import LoginManager, login_user, logout_user, current_user, login_required, UserMixin
from app.user import User

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

@app.route('/chains/<int:chid>', methods=['GET', 'PUT', 'DELETE'])
def handleChainsbyId(chid):
    if request.method == 'GET':
        return BaseChains().getChainsbyId(int(chid))
    elif request.method == 'DELETE':
        return BaseChains().deleteChainbyId(int(chid))
    elif request.method == 'PUT':
        file = request.json
        file["chid"] = int(chid)
        return BaseChains().updateChainbyId(file)
    return "Not reachable!"


@app.route('/client', methods=['GET', 'POST'])
def handleClient():
    if request.method == 'GET':
        return BaseClient().getAllClients()
    elif request.method == 'POST':
        return BaseClient().createClient(request.json)
    return "Not reachable!"

@app.route('/client/<int:clid>', methods=['GET', 'PUT', 'DELETE'])
def handleClientbyId(clid):
    if request.method == 'GET':
        return BaseClient().getClientbyId(int(clid))
    elif request.method == 'DELETE':
        return BaseClient().deleteClientbyId(int(clid))
    elif request.method == 'PUT':
        file = request.json
        file["clid"] = int(clid)
        return BaseClient().updateClientbyId(file)
    return "Not reachable!"


@app.route('/employee', methods=['GET', 'POST'])
def getAllEmployee():
    if request.method == 'GET':
        return BaseEmployee().getAllEmployee()
    elif request.method == 'POST':
        return BaseEmployee().createEmployee(request.json)
    return "Not reachable!"

@app.route('/employee/<int:eid>', methods=['GET', 'PUT', 'DELETE'])
def getEmployeebyId(eid):
    if request.method == 'GET':
        return BaseEmployee().getEmployeebyId(int(eid))
    elif request.method == 'DELETE':
        return BaseEmployee().deleteEmployeebyId(int(eid))
    elif request.method == 'PUT':
       file = request.json
       file["eid"] = int(eid)
       return BaseEmployee().updateEmployeebyId(file)
    return "Not reachable!"


@app.route('/most/revenue', methods=["POST"])
#@login_required
def getTopThreeTotalRevenue():
      if request.method == 'POST':
        return BaseGlobalStatistic().getTopThreeTotalRevenue(request.json)
      return "Not reachable!"

@app.route('/paymentmethod', methods=["POST"])
#@login_required
def ggetpercentageByPaymentMethod():
      if request.method == 'POST':
        return BaseGlobalStatistic().getpercentageByPaymentMethod(request.json)
      return "Not reachable!"
      
@app.route('/least/rooms', methods=["POST"])
#@login_required
def handlergetTopThreeLeastRooms():

    if request.method == 'POST':
        return BaseGlobalStatistic().getTopThreeLeastRooms(request.json)

    return "Not reachable!"

@app.route('/most/capacity', methods=["POST"])
#@login_required
def getTopFiveHotelsMostCapacity():
    if request.method == "POST":
        return BaseGlobalStatistic().getTopFiveHotelsMostCapacity(request.json)

    return "Not reachable!"


@app.route('/most/reservation', methods=["POST"])
#@login_required
def  getTopTenByHotelReservation():
      if request.method == 'POST':
        return BaseGlobalStatistic().getTopTenByHotelReservation(request.json)
      return "Not reachable!"

@app.route('/most/profitmonth', methods=["POST"])
#@login_required
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

@app.route('/hotel/<int:hid>', methods=['GET', 'PUT','DELETE'])
def getHotelbyId(hid):
    if request.method == 'GET':
        return BaseHotel().getHotelbyId(int(hid))
    elif request.method == 'DELETE':
        return BaseHotel().deleteHotelbyId(int(hid))
    elif request.method == 'PUT':
        file = request.json
        file["hid"] = int(hid)
        return BaseHotel().updateHotelbyId(file)
    return "Not reachable!"

@app.route('/hotel/<int:hid>/handicaproom', methods=['POST'])
#@login_required
def handlerTopFiveRoomHandicap(hid):

    if request.method == 'POST':
        return BaseLocalStatistic().obtainTopFiveHandicapReserveRoom(hid, request.json)

    return "Not reachable!"

@app.route('/hotel/<int:hid>/leastreserve', methods=['POST'])
#@login_required
def handlerTopThreeLeastTimeUnavailableRoom(hid):
    if request.method == 'POST':
        return BaseLocalStatistic().obtainTopThreeLeastTimeUnavailableRoom(hid, request.json)
    return "Not reachable!"
    
@app.route('/hotel/<int:hid>/mostcreditcard', methods=['POST'])
#@login_required
def handlerTopFiveMostCreditCard(hid):

    if request.method == "POST":
        return BaseLocalStatistic().obtainTopFiveMostCreditCards(hid, request.json)

    return "Not reachable!"


@app.route('/hotel/<int:hid>/highestpaid', methods=['POST'])
#@login_required
def handlerTopThreeHighestPaidRegularEmployee(hid):

    if request.method == "POST":
        return BaseLocalStatistic().obtainTopThreeHighestPaidRegularEmployee(hid, request.json)

    return "Not reachable!"



@app.route('/hotel/<int:hid>/mostdiscount', methods=['POST'])
#@login_required
def handlerTopFiveClientsMostDiscounts(hid):

    if request.method == "POST":
        return BaseLocalStatistic().obtainTopFiveClientsMostDiscounts(hid, request.json)

    return "Not reachable!"


@app.route('/hotel/<int:hid>/roomtype', methods=['POST'])
#@login_required
def handlerTotalReservationRoomType(hid):
    if request.method == "POST":
        return BaseLocalStatistic().obtainTotalReservationRoomType(hid, request.json)

    return "Not reachable!"


@app.route('/hotel/<int:hid>/leastguests', methods=['POST'])
#@login_required
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

@app.route('/login/<int:lid>', methods=['GET', 'PUT', 'DELETE'])
def handleLoginbyId(lid):
    if request.method == 'GET':
        return BaseLogin().getLoginbyId(int(lid))
    elif request.method == 'DELETE':
        return BaseLogin().deleteLoginbyId(int(lid))
    elif request.method == 'PUT':
        file = request.json
        file["lid"] = int(lid)
        return BaseLogin().updateLoginbyId(file)
    return "Not reachable!"

@app.route('/auth', methods=["GET", "POST"])
def userLogin():    
    if request.method == 'POST':
        data = request.json
        print(data)
        username = data.get('username')
        password = data.get('password')
        #print(data.form['username'])
        #username = data.form['username']
        #password = data.form['password']
        if not username or not password:
            return jsonify({'status': 'error', 'message': 'Missing username or password'}), 400

        user = User(BaseLogin().verifyLogin(username, password))
       
        if user.eid is not None:
            print("User exist:", user,"\n")
            login_user(user)
            print(user.is_authenticated)
            employee_data =  user.get_employee()
            return jsonify({'detail': "Login successful", 'eid': user.eid, 'lname': employee_data['lname'], 'position': employee_data['position']}), 200
        print("Invalid username or password")
        return jsonify({'status': 'Wrong username or password'}), 400
        
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.json

        login = {
            'username': data.get('username'),
            'password': data.get('password')
        }
        if not login['username'] or not login['password']:
            return jsonify({'status': 'Invalid credentials'}), 400
        ## Verify if username already exist

        employee = {
            'fname':  data.get('fname'),
            'lname': data.get('lname'),
            'position': data.get('position'),
            'salary': data.get('salary'),
            'age': data.get('age') 
        }

        ## VErify if empployee already exist??

        if not employee['fname'] or not employee['lname'] or \
           not employee['position'] or not employee['salary'] or not employee['age']:
            return jsonify({'status': 'Invalid credentials'}), 400
        ## Create Login
        BaseLogin.createLogin(login)
        ## Create employee
        BaseEmployee.createEmployee(employee)


@app.route('/signout', methods=["GET"])
#@login_required
def signout():
    logout_user()
    return redirect("login.ipynb")

@app.route('/reserve', methods=['GET', 'POST'])
def handleReserve():
    if request.method == 'GET':
        return BaseReserve().getAllReserve()
    elif request.method == 'POST':
        return BaseReserve().createReserve(request.json)
    return "Not reachable!"

@app.route('/reserve/<int:reid>', methods=['GET', 'PUT', 'DELETE'])
def handleReservebyId(reid):
    if request.method == 'GET':
        return BaseReserve().getReservebyId(int(reid))
    elif request.method == 'DELETE':
        return BaseReserve().deleteReservebyId(int(reid))
    elif request.method == 'PUT':
        file = request.json
        file["reid"] = int(reid)
        return BaseReserve().updateReservebyId(file)
    return "Not reachable!"


@app.route('/room', methods=['GET', 'POST'])
def getAllRoom():
    if request.method == 'GET':
        return BaseRoom().getAllRoom()
    elif request.method == 'POST':
        return BaseRoom().createRoom(request.json)
    return "Not reachable!"

@app.route('/room/<int:rid>', methods=['GET', 'PUT', 'DELETE'])
def getRoombyId(rid):
    if request.method == 'GET':
        return BaseRoom().getRoombyId(int(rid))
    elif request.method == 'DELETE':
        return BaseRoom().deleteRoombyId(int(rid))
    elif request.method == 'PUT':
        file = request.json
        file["rid"] = int(rid)
        return BaseRoom().updateRoombyId(file)
    return "Not reachable!"

@app.route('/roomdescription', methods=['GET', 'POST'])
def handleRoomDescription():
    if request.method == 'GET':
        return BaseRoomDescription().getAllRoomDescription()
    elif request.method == 'POST':
        return BaseRoomDescription().createRoomDescription(request.json)
    return "Not reachable!"

@app.route('/roomdescription/<int:rdid>', methods=['GET', 'PUT', 'DELETE'])
def handleRoomDescriptionbyId(rdid):
    if request.method == 'GET':
        return BaseRoomDescription().getRoomDescriptionbyId(int(rdid))
    elif request.method == 'DELETE':
        return BaseRoomDescription().deleteRoomDescriptionbyId(int(rdid))
    elif request.method == 'PUT':
        file = request.json
        file["rdid"] = int(rdid)
        return BaseRoomDescription().updateRoomDescriptionbyId(file)
    return "Not reachable!"

@app.route('/roomunavailable', methods=['GET', 'POST'])
def getAllRoomUnavailable():
    if request.method == 'GET':
        return BaseRoomUnavailable().getAllRoomUnavailable()
    elif request.method == 'POST':
        return BaseRoomUnavailable().createRoomUnavailable(request.json)
    return "Not reachable!"

@app.route('/roomunavailable/<int:ruid>', methods=['GET', 'PUT', 'DELETE'])
def getRoomUnavailablebyId(ruid):
    if request.method == 'GET':
        return BaseRoomUnavailable().getRoomUnavailablebyId(int(ruid))
    elif request.method == 'DELETE':
        return BaseRoomUnavailable().deleteRoomUnavailablebyId(int(ruid))
    elif request.method == 'PUT':
        file = request.json
        file["ruid"] = int(ruid)
        return BaseRoomUnavailable().updateRoomUnavailablebyId(file)
    return "Not reachable!"

if __name__ == "__main__":
  
    app.run()