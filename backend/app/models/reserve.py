from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation

class ReserveDAO(BaseDAO):
    def getAllReserve(self):
        cur = self.conn.cursor()
        cur.execute("SELECT reid, ruid, clid, total_cost, payment, guests from reserve;")
        result = []
        for row in cur:
            result.append(dict(zip(["reid", "ruid", "clid", "total_cost", "payment", "guests"], row)))
        self.conn.close()
        return result

    def getReservebyId(self, reid):
        cur = self.conn.cursor()
        cur.execute("SELECT reid, ruid, clid, total_cost, payment, guests from reserve where reid = %s;", (reid,))
        result = dict(zip(["reid", "ruid", "clid", "total_cost", "payment", "guests"], cur.fetchone()))
        self.conn.close()
        return result
    
    def createReserve(self, data):
        cur = self.conn.cursor()
        res = None
        while(True):
            try:
                cur.execute("INSERT into reserve (ruid, clid, total_cost, payment, guests) values (%s, %s, %s, %s, %s) returning reid;",
                            (data["ruid"], data["clid"], data["total_cost"], data["payment"], data["guests"]))
                res = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert into Reserve")
            else:
                break
            finally:
                self.conn.commit()
        result = dict(zip(["reid", "ruid", "clid", "total_cost", "payment", "guests"], 
                          (res, data["ruid"], data["clid"], data["total_cost"], data["payment"], data["guests"])))
        self.conn.close()
        return result

    def deleteReservebyId(self, reid):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM reserve where reid = %s;", (reid,))
        self.conn.commit()
        rows = cur.rowcount
        self.conn.close()
        if (rows == 0):
            return ""
        return "Deleted"
    
    def updateReservebyId(self, data):
        cur = self.conn.cursor()
        cur.execute("UPDATE reserve SET ruid = %s, clid =%s, total_cost =%s, payment =%s, guests =%s WHERE reid = %s;",
                            (data["ruid"], data["clid"], data["total_cost"], data["payment"], data["guests"], data["reid"],))
        self.conn.commit()
        self.conn.close()
        return "Updated"