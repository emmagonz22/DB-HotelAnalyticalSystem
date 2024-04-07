from .baseDAO import BaseDAO
class HotelDAO(BaseDAO):
    def getAllHotel(self):
        cur = self.conn.cursor()
        cur.execute("SELECT hid, chid, hname, hcity from hotel;")
        result = []
        for row in cur:
            result.append(dict(zip(["hid", "chid", "hname", "hcity"], row)))
        return result