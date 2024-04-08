from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation
class HotelDAO(BaseDAO):
    def getAllHotel(self):
        cur = self.conn.cursor()
        cur.execute("SELECT hid, chid, hname, hcity from hotel;")
        result = []
        for row in cur:
            result.append(dict(zip(["hid", "chid", "hname", "hcity"], row)))
        return result
    
    def getHotelbyId(self,hid):
        cur=self.conn.cursor()
        cur.execute("SELECT hid, chid, hname, hcity from hotel where hid = %s;", (hid,))
        result=dict(zip(["hid", "chid", "hname", "hcity"], cur.fetchone()))
        self.conn.close()
        return result
    
    # def createHotel(self, data):
    #     cur=self.conn.cursor()
    #     cur.execute("INSERT into hotel (chid, hname, hcity) values (%s, %s, %s, %s) returning hid;",
    #                 (data["chid"], data["hname"], data["hcity"]))
    #     result = cur.fetchone()[0]
    #     self.conn.close()
    #     return result
    
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
            else:
                break
            finally:
                self.conn.commit()
        result=dict(zip(["hid", "chid", "hname", "hcity"],
                        (data,json["chid"],json["hname"],json["hcity"])))
        self.conn.close()
        return result
    
    def deleteHotelbyId(self,hid):
        cur=self.conn.cursor()
        cur.execute("DELETE FROM hotel where hid = %s;", (hid,))
        self.conn.commit()
        if (cur.rowcount == 0):
            return ""
        return "Deleted"
    
    def updateHotelbyId(self,json):
        cur=self.conn.cursor()
        cur.execute("UPDATE hotel SET chid=%s, hname=%s, hcity=%s WHERE hid=%s;",
                    (json["chid"],json["hname"],json["hcity"],json["hid"],))
        self.conn.commit()
        return "Updated"