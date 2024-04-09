from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation

class ChainsDAO(BaseDAO):
    def validateData(self, json, action):
        try:
            chid = None
            if action == "UPDATE":
                chid = json["chid"]
            elif action == "CREATE":
                chid = 0
            cname = json["cname"]
            springmkup = json["springmkup"]
            summermkup = json["summermkup"]
            fallmkup = json["fallmkup"]
            wintermkup = json["wintermkup"]

            return isinstance(chid, int) and isinstance(cname, str) and isinstance(springmkup, float) and isinstance(summermkup, float) and isinstance(fallmkup, float) and isinstance(wintermkup, float) and springmkup >= 0 and summermkup >= 0 and fallmkup >= 0 and wintermkup >= 0
        except Exception as e:
            return False

    def getAllChains(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT chid, cname, springmkup, summermkup, fallmkup, wintermkup from chains;")
        except Exception as e:
            # Always needed
            self.conn.rollback()
            self.conn.close()
            return str(e)
        
        result = []
        for row in cur:
            result.append(dict(zip(["chid", "cname", "springmkup", "summermkup", "fallmkup", "wintermkup"], row)))
        self.conn.close()
        return result

    def getChainsbyId(self, chid):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT chid, cname, springmkup, summermkup, fallmkup, wintermkup from chains where chid = %s;", (chid,))
        except Exception as e:
            # Always needed
            self.conn.rollback()
            self.conn.close()
            return str(e)

        # Always needed
        if (cur.rowcount == 0):
            return "Chain " + str(chid) + " does not exist!"
        result = dict(zip(["chid", "cname", "springmkup", "summermkup", "fallmkup", "wintermkup"], cur.fetchone()))
        self.conn.close()
        return result
    
    def createChain(self, data):
        # Validation of data always needed
        if not self.validateData(data, "CREATE"):
            return "Invalid Parameters have been passed!"
        cur = self.conn.cursor()
        res = None
        while(True):
            try:
                cur.execute("INSERT into chains (cname, springmkup, summermkup, fallmkup, wintermkup) values (%s, %s, %s, %s, %s) returning chid;",
                            (data["cname"], data["springmkup"], data["summermkup"], data["fallmkup"], data["wintermkup"],))
                res = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert into Chains")
            except Exception as e:
                # Always needed
                self.conn.rollback()
                self.conn.close()
                return str(e)
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
        try:
            cur.execute("DELETE FROM chains where chid = %s;", (chid,))
        except Exception as e:
            # Always needed
            self.conn.rollback()
            self.conn.close()
            return str(e)
        self.conn.commit()
        self.conn.close()
        if (cur.rowcount == 0):
            return "Chain " + str(chid) + " does not exist!"
        return "Deleted " + str(chid)
    
    def updateChainbyId(self, data):
        # Validation of data always needed
        if not self.validateData(data, "UPDATE"):
            return "Invalid Parameters have been passed!"
        cur = self.conn.cursor()
        try:
            cur.execute("UPDATE chains SET cname = %s, springmkup =%s, summermkup =%s, fallmkup =%s, wintermkup=%s WHERE chid = %s;",
                                (data["cname"], data["springmkup"], data["summermkup"], data["fallmkup"], data["wintermkup"], data["chid"],))
        except Exception as e:
            # Always needed
            self.conn.rollback()
            self.conn.close()
            return str(e)
        self.conn.commit()
        self.conn.close()
        return "Updated " + str(data["chid"])