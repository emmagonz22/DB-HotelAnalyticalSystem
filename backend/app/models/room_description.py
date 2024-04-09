from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation

class RoomDescriptionDAO(BaseDAO):
    def getAllRoomDescription(self):
        cur = self.conn.cursor()
        cur.execute("SELECT rdid, rname, rtype, capacity, ishandicap from roomdescription;")
        result = []
        for row in cur:
            result.append(dict(zip(["rdid", "rname", "rtype", "capacity", "ishandicap"], row)))
        self.conn.close()
        return result

    def getRoomDescriptionbyId(self, rdid):
        cur = self.conn.cursor()
        cur.execute("SELECT rdid, rname, rtype, capacity, ishandicap from roomdescription where rdid = %s;", (rdid,))
        result = dict(zip(["rdid", "rname", "rtype", "capacity", "ishandicap"], cur.fetchone()))
        self.conn.close()
        return result
    
    def createRoomDescription(self, data):
        cur = self.conn.cursor()
        res = None
        while(True):
            try:
                cur.execute("INSERT into roomdescription (rname, rtype, capacity, ishandicap) values (%s, %s, %s, %s) returning rdid;",
                            (data["rname"], data["rtype"], data["capacity"], data["ishandicap"],))
                res = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert into Room Description")
            else:
                break
            finally:
                self.conn.commit()
        result = dict(zip(["rdid", "rname", "rtype", "capacity", "ishandicap"], 
                          (res, data["rname"], data["rtype"], data["capacity"], data["ishandicap"])))
        self.conn.close()
        return result

    def deleteRoomDescriptionbyId(self, rdid):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM roomdescription where rdid = %s;", (rdid,))
        self.conn.commit()
        rows = cur.rowcount
        self.conn.close()
        if (rows == 0):
            return ""
        return "Deleted"
    
    def updateRoomDescriptionbyId(self, data):
        cur = self.conn.cursor()
        cur.execute("UPDATE roomdescription SET rname = %s, rtype =%s, capacity =%s, ishandicap =%s WHERE rdid = %s;",
                            (data["rname"], data["rtype"], data["capacity"], data["ishandicap"], data["rdid"],))
        self.conn.commit()
        self.conn.close()
        return "Updated"