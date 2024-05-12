from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation

class LoginDAO(BaseDAO):
    def validateData(self, json, action):
        try:
            lid = None
            eid = json["eid"]
            if action == "UPDATE":
                lid = json["lid"]
            elif action == "CREATE":
                lid = 1
                cur = self.conn.cursor()
                cur.execute("SELECT lid, eid, username, password from login where eid=%s;", (eid,))
                employee = cur.fetchone()
                if employee:
                    return False

            username = json["username"]
            password = json["password"]

            # TODO: NEEDS TO VALIDATE THAT THE LOGIN IS AVAILABLE FOR THAT EMPLOYEE
            # NEEDS TO HAVE A ONE TO ONE RELATIONSHIP

            return isinstance(lid, int) and isinstance(eid, int) and isinstance(username, str) and isinstance(password, str)
        except Exception as e:
            return False

    def getAllLogin(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT lid, eid, username, password from login;")
        except Exception as e:
            self.conn.rollback()
            self.conn.close()
            return str(e)
        result = []
        for row in cur:
            result.append(dict(zip(["lid", "eid", "username", "password"], row)))
        self.conn.close()   
        return result

    def getLoginbyId(self, lid):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT lid, eid, username, password from login WHERE lid = %s;", (lid,))
        except Exception as e:
            # Always needed
            self.conn.rollback()
            self.conn.close()
            return str(e)
        
        rows = cur.rowcount
        info = cur.fetchone()
        self.conn.close()
        # Always needed
        if (rows == 0):
            return "Login " + str(lid) + " does not exist!"
        result = dict(zip(["lid", "eid", "username", "password"], info))
        return result

    def createLogin(self, data):
        # Validation of data always needed
        if not self.validateData(data, "CREATE"):
            return "Invalid Parameters have been passed!"
        cur = self.conn.cursor()
        res = None # Response when the login is created with the lid of the new inserted value
        while(True):
            try:
                cur.execute("INSERT into login (eid, username, password) values ( %s, %s, %s) returning lid;",
                ( data["eid"], data["username"], data["password"],))
                res = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert into login")
                self.conn.commit()
            except Exception as e:
                # Always needed
                self.conn.rollback()
                self.conn.close()
                return str(e)
            else:
                break

        result = dict(zip(["lid", "eid", "username", "password"], (res, data["eid"], data["username"], data["password"])))
        self.conn.commit()
        self.conn.close()
        return result
    
    def updateLoginbyId(self, json):
        if not self.validateData(json, "UPDATE"):
            return "Invalid parameters have been passed!"
        cur = self.conn.cursor()
        try:
            cur.execute("UPDATE login SET eid = %s, username = %s, password = %s WHERE lid = %s;", (json['eid'],json['username'], json['password'], json['lid']))
        except Exception as e:
            # Always needed
            self.conn.rollback()
            self.conn.close()
            return str(e)
        
        self.conn.commit()
        rows = cur.rowcount
        self.conn.close()
        # Always needed
        if (rows == 0):
            return "Login " + str(json["lid"]) + " does not exist!"
        return "Updated " + str(json["lid"])

    def deleteLoginbyId(self, lid):
        cur = self.conn.cursor()
        try: 
            cur.execute("DELETE FROM login WHERE lid = %s;", (lid,))
        except Exception as e:
            # Always needed
            self.conn.rollback()
            self.conn.close()
            return str(e)
        
        self.conn.commit()
        rows = cur.rowcount
        self.conn.close()
        # Always needed
        if (rows == 0):
            return "Login " + str(lid) + " does not exist!"
        return "Deleted " + str(lid)
