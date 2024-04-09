from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation
class HotelDAO(BaseDAO):
    def validateData(self, json, action):
        try:
            hid = None
            if action == "UPDATE":
                hid = json["hid"]
            elif action == "CREATE":
                hid = 0
            chid = json["chid"]
            hname = json["hname"]
            hcity = json["hcity"]
            return isinstance(hid, int) and isinstance(chid, int) and isinstance(hname, str) and isinstance(hcity, str)
        except Exception as e:
            return False

    def getAllHotel(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT hid, chid, hname, hcity from hotel;")
        except Exception as e:
            self.conn.rollback()
            self.conn.close()
            return str(e)
        result = []
        for row in cur:
            result.append(dict(zip(["hid", "chid", "hname", "hcity"], row)))
        self.conn.close()
        return result

    def getHotelbyId(self,hid):
        cur=self.conn.cursor()
        try:
            cur.execute("SELECT hid, chid, hname, hcity from hotel where hid = %s;", (hid,))
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
            return "Hotel " + str(hid) + " does not exist!"
        result=dict(zip(["hid", "chid", "hname", "hcity"], info))
        return result

    def createHotel(self,json):
        cur=self.conn.cursor()
        data=None
        while(True):
            try:
                cur.execute("INSERT INTO hotel(chid, hname, hcity) values (%s, %s, %s) returning hid;",
                            (json["chid"], json["hname"], json["hcity"],))
                data=cur.fetchone()[0]
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
        result=dict(zip(["hid", "chid", "hname", "hcity"],
                        (data,json["chid"],json["hname"],json["hcity"])))
        self.conn.commit()
        self.conn.close()
        return result
    
    def deleteHotelbyId(self,hid):
        cur=self.conn.cursor()
        try:
            cur.execute("DELETE FROM hotel where hid = %s;", (hid,))
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
            return "Hotel " + str(hid) + " does not exist!"
        return "Deleted " + str(hid)
    
    def updateHotelbyId(self,json):
        if not self.validateData(json, "UPDATE"):
            return "Invalid parameters have been passed!"
        cur=self.conn.cursor()
        try:
            cur.execute("UPDATE hotel SET chid=%s, hname=%s, hcity=%s WHERE hid=%s;",
                        (json["chid"],json["hname"],json["hcity"],json["hid"],))
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
            return "Hotel " + str(json["hid"]) + " does not exist!"
        return "Updated " + str(json["hid"])