from .baseDAO import BaseDAO

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
        cur.execute("INSERT into chains (cname, springmkup, summermkup, fallmkup, wintermkup) values (%s, %s, %s, %s, %s, %s) returning chid;",
                    (data["cname"], data["springmkup"], data["summermkup"], data["fallmkup"], data["wintermkup"]))
        result = cur.fetchone()[0]
        self.conn.close()
        return result
