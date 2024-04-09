import json
from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation

class LoginDAO(BaseDAO):

    def getAllLogin(self):
        cur = self.conn.cursor()
        cur.execute("SELECT lid, eid, username, password from login;")
        result = []
        for row in cur:
            result.append(dict(zip(["lid", "eid", "username", "password"], row)))
        self.conn.close()   
        return result

    def getLoginbyId(self, lid):

        try:
            with self.conn.cursor() as cur:
                cur.execute("SELECT lid, eid, username, password from login WHERE lid = %s;", (lid,))
                res = cur.fetchone()
                if res:
                    result = dict(zip(["lid", "eid", "username", "password"], res))
                else:
                    result = None
            return result
        except Exception as e:
            raise e  
        finally:
            self.conn.close() 
      

    def createLogin(self, data):
        res = None # Response when the login is created with the lid of the new inserted value
        with self.conn.cursor() as cur:
            while(True):
                try:
                    cur.execute("INSERT into login (eid, username, password) values ( %s, %s, %s) returning lid;",
                    ( data["eid"], data["username"], data["password"],))
                    res = cur.fetchone()[0]
                except UniqueViolation as e:
                    print("Retrying to insert into login")
                else:
                    break
                finally:
                    self.conn.commit()

        result = dict(zip(["lid", "eid", "username", "password"], (res, data["eid"], data["username"], data["password"])))
        return result
    
    def updateLoginbyId(self, json):
        cur = self.conn.cursor()
        try:
            cur.execute("UPDATE login SET eid = %s, username = %s, password = %s WHERE lid = %s;", (json['eid'],json['username'], json['password'], json['lid']))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback() # Rollback error if an exception occur after the commit is done
            raise e
        finally: 
            self.conn.close()
            return "Updated"
    def deleteLoginbyId(self, lid):
        cur = self.conn.cursor()
        try: 
            cur.execute("DELETE FROM login WHERE lid = %s;", (lid,))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            self.conn.close()
            if cur.rowcount == 0:
                return 0
            return "Deleted"
