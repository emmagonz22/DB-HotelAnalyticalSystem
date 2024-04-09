from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation

class RoomDescriptionDAO(BaseDAO):
    # Validates input given by user
    def validateData(self, json, action):
        try:
            rdid = None
            if action == "UPDATE":
                rdid = json["rdid"]
            elif action == "CREATE":
                rdid = 0
            rname = json["rname"]
            rtype = json["rtype"]
            capacity = json["capacity"]
            ishandicap = json["ishandicap"]

            if not (isinstance(rdid, int) and isinstance(ishandicap, bool)):
                return False

            if (rname == "Standard"):
                return (capacity == 1) and (rtype == "Basic" or rtype == "Premium")
            elif (rname == "Standard Queen"):
                return (capacity == 1 or capacity == 2) and (rtype == "Basic" or rtype == "Premium" or rtype == "Deluxe")
            elif (rname == "Standard King"):
                return (capacity == 2) and (rtype == "Basic" or rtype == "Premium" or rtype == "Deluxe")
            elif (rname == "Double Queen"):
                return (capacity == 4) and (rtype == "Basic" or rtype == "Premium" or rtype == "Deluxe")
            elif (rname == "Double King"):
                return (capacity == 4 or capacity == 6) and (rtype == "Basic" or rtype == "Premium" or rtype == "Deluxe" or rtype == "Suite")
            elif (rname == "Triple King"):
                return (capacity == 6) and (rtype == "Deluxe" or rtype == "Suite")
            elif (rname == "Executive Family"):
                return (capacity == 4 or capacity == 6 or capacity == 8) and (rtype == "Deluxe" or rtype == "Suite")
            elif (rname == "Presidential"):
                return (capacity == 4 or capacity == 6 or capacity == 8) and (rtype == "Suite")
            else:
                return False
        except Exception as e:
            return False

    def getAllRoomDescription(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT rdid, rname, rtype, capacity, ishandicap from roomdescription;")
        except Exception as e:
            self.conn.rollback()
            self.conn.close()
            return str(e)
        result = []
        for row in cur:
            result.append(dict(zip(["rdid", "rname", "rtype", "capacity", "ishandicap"], row)))
        self.conn.close()
        return result

    def getRoomDescriptionbyId(self, rdid):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT rdid, rname, rtype, capacity, ishandicap from roomdescription where rdid = %s;", (rdid,))
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
            return "Room Description " + str(rdid) + " does not exist!"
        result = dict(zip(["rdid", "rname", "rtype", "capacity", "ishandicap"], info))
        return result
    
    def createRoomDescription(self, data):
        # Validation of data always needed
        if not self.validateData(data, "CREATE"):
            return "Invalid Parameters have been passed!"
        cur = self.conn.cursor()
        res = None
        while(True):
            try:
                cur.execute("INSERT into roomdescription (rname, rtype, capacity, ishandicap) values (%s, %s, %s, %s) returning rdid;",
                            (data["rname"], data["rtype"], data["capacity"], data["ishandicap"],))
                res = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert into Room Description")
                self.conn.commit()
            except Exception as e:
                # Always needed
                self.conn.rollback()
                self.conn.close()
                return str(e)
            else:
                break
        result = dict(zip(["rdid", "rname", "rtype", "capacity", "ishandicap"], 
                          (res, data["rname"], data["rtype"], data["capacity"], data["ishandicap"])))
        self.conn.commit()
        self.conn.close()
        return result

    def deleteRoomDescriptionbyId(self, rdid):
        cur = self.conn.cursor()
        # Always encapsulate in try
        try:
            cur.execute("DELETE FROM roomdescription where rdid = %s;", (rdid,))
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
            return "Room Description " + str(rdid) + " does not exist!"
        return "Deleted " + str(rdid)
    
    def updateRoomDescriptionbyId(self, data):
        if not self.validateData(data, "UPDATE"):
            return "Invalid parameters have been passed!"
        cur = self.conn.cursor()
        try:
            cur.execute("UPDATE roomdescription SET rname = %s, rtype =%s, capacity =%s, ishandicap =%s WHERE rdid = %s;",
                                (data["rname"], data["rtype"], data["capacity"], data["ishandicap"], data["rdid"],))
        except Exception as e:
            # Always needed
            self.conn.rollback()
            self.conn.close()
            return str(e)
        
        self.conn.commit()
        self.conn.close()
        return "Updated " + str(data["rdid"])