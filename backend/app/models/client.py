from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation

class ClientDAO(BaseDAO):
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
        cur.execute("SELECT clid, fname, lname, age, memberyear from client where clid = %s;", (clid,))
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
            else:
                break
            finally:
                self.conn.commit()
        result = dict(zip(["clid", "fname", "lname", "age", "memberyear"], 
                          (res, data["fname"], data["lname"], data["age"], data["memberyear"])))
        self.conn.close()
        return result

    def deleteClientbyId(self, clid):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM client where clid = %s;", (clid,))
        self.conn.commit()
        self.conn.close()
        if (cur.rowcount == 0):
            return ""
        return "Deleted"
    
    def updateClientbyId(self, data):
        cur = self.conn.cursor()
        cur.execute("UPDATE client SET fname = %s, lname =%s, age =%s, memberyear =%s WHERE clid = %s;",
                            (data["fname"], data["lname"], data["age"], data["memberyear"], data["clid"],))
        self.conn.commit()
        self.conn.close()
        return "Updated"