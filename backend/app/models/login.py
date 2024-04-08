import json

class LoginDAO(BaseDAO):

    def getAllLogin():
        cur = self.conn.cursor()
        cur.execute("SELECT lid, eid, username, password from employee;")
        result = []
        for row in cur:
            result.append(dict(zip(["lid", "eid", "username", "password"], row)))
        return result

    def getLoginbyId(id):
        cur = self.conn.cursor()
        cur.execute(f"SELECT lid, eid, username, password from employee WHERE lid = f{id} ;")

        login = zip(["lid", "eid", "username", "password"], cur)


    def createLogin():
        pass
    
    def updateLoginbyId():
        pass

    def deleteLoginbyId():
        pass

