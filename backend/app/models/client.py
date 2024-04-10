from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation

class ClientDAO(BaseDAO):
    # Validates input given by user
    def validateData(self, json, action):
        try:
            clid = None
            if action == "UPDATE":
                clid = json["clid"]
            elif action == "CREATE":
                clid = 1
            fname = json["fname"]
            lname = json["lname"]
            age = json["age"]
            memberyear = json["memberyear"]

            if not (isinstance(clid, int) and isinstance(fname, str) and isinstance(lname, str) and isinstance(age, int) and isinstance(memberyear, int)):
                return False
            
            return age > 0 and memberyear >= 0

        except Exception as e:
            print(str(e))
            return False

    def getAllClients(self):
        cur = self.conn.cursor()
        cur.execute("SELECT clid, fname, lname, age, memberyear from client;")
        result = []
        for row in cur:
            result.append(dict(zip(["clid", "fname", "lname", "age", "memberyear"], row)))
        self.conn.close()
        return result

    def getClientbyId(self, clid):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT clid, fname, lname, age, memberyear from client where clid = %s;", (clid,))
        except Exception as e:
            self.conn.rollback()
            self.conn.close()
            return str(e)
        result = dict(zip(["clid", "fname", "lname", "age", "memberyear"], cur.fetchone()))
        self.conn.close()
        return result
    
    def createClient(self, data):
        cur = self.conn.cursor()
        res = None
        while(True):
            try:
                cur.execute("INSERT into client (fname, lname, age, memberyear) values (%s, %s, %s, %s) returning clid;",
                            (data["fname"], data["lname"], data["age"], data["memberyear"],))
                res = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert into Client")
                self.conn.commit()
            except Exception as e:
                # Always needed
                self.conn.rollback()
                self.conn.close()
                return str(e)
            else:
                break
        result = dict(zip(["clid", "fname", "lname", "age", "memberyear"], 
                          (res, data["fname"], data["lname"], data["age"], data["memberyear"])))
        self.conn.commit()
        self.conn.close()
        return result

    def deleteClientbyId(self, clid):
        cur = self.conn.cursor()
        try:
            cur.execute("DELETE FROM client where clid = %s;", (clid,))
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
            return "Client " + str(clid) + " does not exist!"
        return "Deleted " + str(clid)
    
    def updateClientbyId(self, data):
        if not self.validateData(data, "UPDATE"):
            return "Invalid parameters have been passed!"
        cur = self.conn.cursor()
        try:
            cur.execute("UPDATE client SET fname = %s, lname =%s, age =%s, memberyear =%s WHERE clid = %s;",
                                (data["fname"], data["lname"], data["age"], data["memberyear"], data["clid"],))
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
            return "Client " + str(data["clid"]) + " does not exist!"
        return "Updated " + str(data["clid"])