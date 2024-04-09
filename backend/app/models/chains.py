from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation

class ChainsDAO(BaseDAO):
    def getAllChains(self):
        cur = self.conn.cursor()
        cur.execute("SELECT chid, cname, springmkup, summermkup, fallmkup, wintermkup from chains;")
        result = []
        for row in cur:
            result.append(dict(zip(["chid", "cname", "springmkup", "summermkup", "fallmkup", "wintermkup"], row)))
        self.conn.close()
        return result

    def getChainsbyId(self, chid):
        cur = self.conn.cursor()
        cur.execute("SELECT chid, cname, springmkup, summermkup, fallmkup, wintermkup from chains where chid = %s;", (chid,))
        result = dict(zip(["chid", "cname", "springmkup", "summermkup", "fallmkup", "wintermkup"], cur.fetchone()))
        self.conn.close()
        return result
    
    def createChain(self, data):
        cur = self.conn.cursor()
        res = None
        while(True):
            try:
                cur.execute("INSERT into chains (cname, springmkup, summermkup, fallmkup, wintermkup) values (%s, %s, %s, %s, %s) returning chid;",
                            (data["cname"], data["springmkup"], data["summermkup"], data["fallmkup"], data["wintermkup"],))
                res = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert into Chains")
            else:
                break
            finally:
                self.conn.commit()
        result = dict(zip(["chid", "cname", "springmkup", "summermkup", "fallmkup", "wintermkup"], 
                          (res, data["cname"], data["springmkup"], data["summermkup"], data["fallmkup"], data["wintermkup"])))
        self.conn.close()
        return result

    def deleteChainbyId(self, chid):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM chains where chid = %s;", (chid,))
        self.conn.commit()
        self.conn.close()
        if (cur.rowcount == 0):
            return ""
        return "Deleted"
    
    def updateChainbyId(self, data):
        cur = self.conn.cursor()
        cur.execute("UPDATE chains SET cname = %s, springmkup =%s, summermkup =%s, fallmkup =%s, wintermkup=%s WHERE chid = %s;",
                            (data["cname"], data["springmkup"], data["summermkup"], data["fallmkup"], data["wintermkup"], data["chid"],))
        self.conn.commit()
        self.conn.close()
        return "Updated"