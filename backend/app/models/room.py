from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation
class RoomDAO(BaseDAO):
    def getAllRoom(self):
        cur = self.conn.cursor()
        cur.execute("SELECT rid, hid, rdid, rprice from room;")
        result = []
        for row in cur:
            result.append(dict(zip(["rid", "hid", "rdid", "rprice"], row)))
        return result
    
    def getRoombyId(self,rid):
        cur = self.conn.cursor()
        cur.execute("SELECT rid, hid, rdid, rprice from room where rid = %s;", (rid,))
        result = []
        for row in cur:
            result.append(dict(zip(["rid", "hid", "rdid", "rprice"], row)))
        return result
    
    def createRoom(self, json):
        cur = self.conn.cursor()
        data = None
        while(True):
            try:
                cur.execute("INSERT INTO room(hid, rdid, rprice) values (%s, %s, %s) returning rid;",
                            (json["hid"], json["rdid"], json["rprice"],))
                data = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert")
            else:
                break
            finally:
                self.conn.commit()
        result = dict(zip(["rid", "hid", "rdid", "rprice"], 
                          (data, json["hid"], json["rdid"], json["rprice"])))
        self.conn.close()
        return result

    def deleteRoombyId(self,rid):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM room where rid = %s;", (rid,))
        self.conn.commit()
        if (cur.rowcount == 0):
            return ""
        return "Deleted"
    
    def updateRoombyId(self, json):
        cur = self.conn.cursor()
        cur.execute("UPDATE room SET hid = %s, rdid =%s, rprice =%s WHERE rid = %s;",
                            (json["hid"], json["rdid"], json["rprice"],json["rid"],))
        self.conn.commit()
        return "Updated"