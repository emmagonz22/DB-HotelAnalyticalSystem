from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation
class RoomDAO(BaseDAO):
    def validateData(self, json, action):
        try:
            rid = None
            if action == "UPDATE":
                rid = json["rid"]
            elif action == "CREATE":
                rid = 0
            hid = json["hid"]
            rdid = json["rdid"]
            rprice = json["rprice"]

            if not (isinstance(rid, int) and isinstance(hid, int) and isinstance(rdid, int) and isinstance(rprice, float)):
                return False
            return rprice > 0
        except Exception as e:
            return False

    def getAllRoom(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT rid, hid, rdid, rprice from room;")
        except Exception as e:
            self.conn.rollback()
            self.conn.close()
            return str(e)
        result = []
        for row in cur:
            result.append(dict(zip(["rid", "hid", "rdid", "rprice"], row)))
        self.conn.close()
        return result
    
    def getRoombyId(self,rid):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT rid, hid, rdid, rprice from room where rid = %s;", (rid,))
        except Exception as e:
            self.conn.rollback()
            self.conn.close()
            return str(e)
        
        rows = cur.rowcount
        info = cur.fetchone()
        self.conn.close()
        # Always needed
        if (rows == 0):
            return "Room " + str(rid) + " does not exist!"
        result = dict(zip(["rid", "hid", "rdid", "rprice"], info))
        self.conn.close()
        return result
    
    def createRoom(self, json):
        # Validation of data always needed
        if not self.validateData(json, "CREATE"):
            return "Invalid Parameters have been passed!"
        cur = self.conn.cursor()
        data = None
        while(True):
            try:
                cur.execute("INSERT INTO room(hid, rdid, rprice) values (%s, %s, %s) returning rid;",
                            (json["hid"], json["rdid"], json["rprice"],))
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
        result = dict(zip(["rid", "hid", "rdid", "rprice"], 
                          (data, json["hid"], json["rdid"], json["rprice"])))
        self.conn.commit()
        self.conn.close()
        return result

    def deleteRoombyId(self,rid):
        cur = self.conn.cursor()
        try:
            cur.execute("DELETE FROM room where rid = %s;", (rid,))
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
            return "Room " + str(rid) + " does not exist!"
        return "Deleted " + str(rid)
    
    def updateRoombyId(self, json):
        if not self.validateData(json, "UPDATE"):
            return "Invalid parameters have been passed!"
        cur = self.conn.cursor()
        try:
            cur.execute("UPDATE room SET hid = %s, rdid =%s, rprice =%s WHERE rid = %s;",
                                (json["hid"], json["rdid"], json["rprice"],json["rid"],))
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
            return "Room " + str(json["rid"]) + " does not exist!"
        return "Updated " + str(json["rid"])