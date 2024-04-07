from .baseDAO import BaseDAO

class ChainsDAO(BaseDAO):
    def getAllChains(self):
        cur = self.conn.cursor()
        cur.execute("SELECT chid, cname, springmkup, summermkup, fallmkup, wintermkup from chains;")
        result = []
        for row in cur:
            result.append(dict(zip(["chid", "cname", "springmkup", "summermkup", "fallmkup", "wintermkup"], row)))
        return result
