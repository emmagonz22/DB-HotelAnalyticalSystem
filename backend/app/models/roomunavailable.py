from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation
from datetime import datetime
class RoomUnavailableDAO(BaseDAO):
    def validateData(self, json, action):
        try:
            ruid = None
            if action == "UPDATE":
                ruid = json["ruid"]
            elif action == "CREATE":
                ruid = 0
            rid = json["rid"]
            startdate = str(json["startdate"])
            enddate = str(json["enddate"])

            if not (isinstance(ruid, int) and isinstance(rid, int)):
                return False

            cur = self.conn.cursor()
            cur.execute("select cast(%s as date) > cast(%s as date) as days", (startdate, enddate,))
            if cur.fetchone()[0]:
                return False
            if action == "CREATE":
                cur.execute("SELECT * from roomunavailable where rid = %s and ((startdate BETWEEN %s AND %s) or (enddate BETWEEN %s AND %s) or (%s BETWEEN startdate AND enddate))", (rid, startdate, enddate, startdate, enddate, enddate,))
            elif action == "UPDATE":
                cur.execute("SELECT * from roomunavailable where ruid <> %s and rid = %s and ((startdate BETWEEN %s AND %s) or (enddate BETWEEN %s AND %s) or (%s BETWEEN startdate AND enddate))", (ruid, rid, startdate, enddate, startdate, enddate, enddate,))
            rows = cur.rowcount
            print(rows)


            return rows == 0

        except Exception as e:
            print(str(e))
            return False

    def getAllRoomUnavailable(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT ruid, rid, startdate, enddate from roomunavailable;")
        except Exception as e:
            self.conn.rollback()
            self.conn.close()
            return str(e)
        result = []
        for row in cur:
            result.append(dict(zip(["ruid", "rid", "startdate", "enddate"], row)))
        self.conn.close()
        return result
    
    def getRoomUnavailablebyId(self,ruid):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT ruid, rid, startdate, enddate from roomunavailable where ruid = %s;", (ruid,))
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
            return "Room Unavailable " + str(ruid) + " does not exist!"
        result = dict(zip(["ruid", "rid", "startdate", "enddate"], info))
        return result
    
    def createRoomUnavailable(self, json):
        # Validation of data always needed
        if not self.validateData(json, "CREATE"):
            return "Invalid Parameters have been passed!"
        cur = self.conn.cursor()
        data = None
        while(True):
            try:
                cur.execute("INSERT INTO roomunavailable(rid, startdate, enddate) values (%s, %s, %s) returning ruid;",
                            (json["rid"], json["startdate"], json["enddate"],))
                data = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert")
                self.conn.commit()
            except Exception as e:
                # Always needed
                self.conn.rollback()
                self.conn.close()
                return str(e)
            else:
                break
        result = dict(zip(["ruid", "rid", "startdate", "enddate"], 
                          (data, json["rid"], json["startdate"], json["enddate"])))
        self.conn.commit()
        self.conn.close()
        return result

    def deleteRoomUnavailablebyId(self,ruid):
        cur = self.conn.cursor()
        try:
            cur.execute("DELETE FROM roomunavailable where ruid = %s;", (ruid,))
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
            return "Room Unavailable " + str(ruid) + " does not exist!"
        return "Deleted " + str(ruid)
    
    def updateRoomUnavailablebyId(self, json):
        if not self.validateData(json, "UPDATE"):
            return "Invalid parameters have been passed!"
        cur = self.conn.cursor()
        try:
            cur.execute("UPDATE roomunavailable SET rid= %s, startdate=%s, enddate=%s WHERE ruid= %s;",
                                (json["rid"], json["startdate"], json["enddate"],json["ruid"],))
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
            return "Room Unavailable " + str(json["ruid"]) + " does not exist!"
        return "Updated " + str(json["ruid"])