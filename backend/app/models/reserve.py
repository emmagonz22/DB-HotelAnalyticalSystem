from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation

class ReserveDAO(BaseDAO):
    def validateData(self, json, action):
        try:
            reid = None
            if action == "UPDATE":
                reid = json["reid"]
            elif action == "CREATE":
                reid = 1
            ruid = json["ruid"]
            clid = json["clid"]
            total_cost = json["total_cost"]
            payment = json["payment"]
            guests = json["guests"]

            if not (isinstance(reid, int) and isinstance(ruid, int) and isinstance(clid, int) and isinstance(total_cost, float) and isinstance(payment, str) and isinstance(guests, int)):
                return False
            
            if not (payment == "cash" or payment == "check" or payment == "credit card" or payment == "debit card" or payment == "pear pay" or guests > 0):
                return False
            
            cur = self.conn.cursor()
            cur.execute("select rprice, (enddate - startdate) as days, extract(month from startdate) as month, springmkup, summermkup, fallmkup, wintermkup, memberyear, capacity from reserve natural inner join roomunavailable natural inner join room natural inner join client natural inner join hotel natural inner join chains natural inner join roomdescription where ruid = %s;", (ruid,))

            values = dict(zip(["rprice", "days", "month", "springmkup", "summermkup", "fallmkup", "wintermkup", "memberyear", "capacity"], cur.fetchone()))
            print(values)
            season = None
            month = int(values["month"])
            if guests > values["capacity"]:
                return False
            print(month)
            if (month <= 5 and month >= 3):
                season = values["springmkup"]
            elif (month <= 8 and month >= 6):
                season = values["summermkup"]
            elif (month <= 11 and month >= 9):
                season = values["fallmkup"]
            elif (month <= 2 and month >= 12):
                season = values["wintermkup"]
            print(season)

            discount = 0
            memyear = values["memberyear"]
            if memyear <= 4:
                discount = 0.98
            elif memyear <= 9:
                discount = 0.95
            elif memyear <= 14:
                discount = 0.92
            else:
                discount = 0.88
            cost = int(values["days"]) * values["rprice"] * season * discount
            return int(cost) == int(total_cost)
        except Exception as e:
            print(str(e))
            return False
        
    def getAllReserve(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT reid, ruid, clid, total_cost, payment, guests from reserve;")
        except Exception as e:
            self.conn.rollback()
            self.conn.close()
            return str(e)
        result = []
        for row in cur:
            result.append(dict(zip(["reid", "ruid", "clid", "total_cost", "payment", "guests"], row)))
        self.conn.close()
        return result

    def getReservebyId(self, reid):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT reid, ruid, clid, total_cost, payment, guests from reserve where reid = %s;", (reid,))
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
            return "Reserve " + str(reid) + " does not exist!"
        result = dict(zip(["reid", "ruid", "clid", "total_cost", "payment", "guests"], info))
        return result
    
    def createReserve(self, data):
        # Validation of data always needed
        if not self.validateData(data, "CREATE"):
            return "Invalid Parameters have been passed!"
        cur = self.conn.cursor()
        res = None
        while(True):
            try:
                cur.execute("INSERT into reserve (ruid, clid, total_cost, payment, guests) values (%s, %s, %s, %s, %s) returning reid;",
                            (data["ruid"], data["clid"], data["total_cost"], data["payment"], data["guests"]))
                res = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert into Reserve")
                self.conn.commit()
            except Exception as e:
                # Always needed
                self.conn.rollback()
                self.conn.close()
                return str(e)
            else:
                break
        result = dict(zip(["reid", "ruid", "clid", "total_cost", "payment", "guests"], 
                          (res, data["ruid"], data["clid"], data["total_cost"], data["payment"], data["guests"])))
        self.conn.commit()
        self.conn.close()
        return result

    def deleteReservebyId(self, reid):
        cur = self.conn.cursor()
        try:
            cur.execute("DELETE FROM reserve where reid = %s;", (reid,))
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
            return "Reserve " + str(reid) + " does not exist!"
        return "Deleted " + str(reid)
    
    def updateReservebyId(self, data):
        if not self.validateData(data, "UPDATE"):
            return "Invalid parameters have been passed!"
        cur = self.conn.cursor()
        try:
            cur.execute("UPDATE reserve SET ruid = %s, clid =%s, total_cost =%s, payment =%s, guests =%s WHERE reid = %s;",
                                (data["ruid"], data["clid"], data["total_cost"], data["payment"], data["guests"], data["reid"],))
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
            return "Reserve " + str(data["reid"]) + " does not exist!"
        return "Updated " + str(data["reid"])