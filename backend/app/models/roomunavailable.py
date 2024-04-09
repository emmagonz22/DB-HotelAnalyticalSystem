from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation
class RoomUnavailableDAO(BaseDAO):
    def getAllRoomUnavailable(self):
        cur = self.conn.cursor()
        cur.execute("SELECT ruid, rid, startdate, enddate from roomunavailable;")
        result = []
        for row in cur:
            result.append(dict(zip(["ruid", "rid", "startdate", "enddate"], row)))
        return result
    
    def getRoomUnavailablebyId(self,ruid):
        cur = self.conn.cursor()
        cur.execute("SELECT ruid, rid, startdate, enddate from roomunavailable where ruid = %s;", (ruid,))
        result = []
        for row in cur:
            result.append(dict(zip(["ruid", "rid", "startdate", "enddate"], row)))
        return result
    
    def createRoomUnavailable(self, json):
        cur = self.conn.cursor()
        data = None
        while(True):
            try:
                cur.execute("INSERT INTO roomunavailable(rid, startdate, enddate) values (%s, %s, %s) returning ruid;",
                            (json["rid"], json["startdate"], json["enddate"],))
                data = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert")
            else:
                break
            finally:
                self.conn.commit()
        result = dict(zip(["ruid", "rid", "startdate", "enddate"], 
                          (data, json["rid"], json["startdate"], json["enddate"])))
        self.conn.close()
        return result

    def deleteRoomUnavailablebyId(self,ruid):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM roomunavailable where ruid = %s;", (ruid,))
        self.conn.commit()
        if (cur.rowcount == 0):
            return ""
        return "Deleted"
    
    def updateRoomUnavailablebyId(self, json):
        cur = self.conn.cursor()
        cur.execute("UPDATE roomunavailable SET rid= %s, startdate=%s, enddate=%s WHERE ruid= %s;",
                            (json["rid"], json["startdate"], json["enddate"],json["ruid"],))
        self.conn.commit()
        return "Updated"