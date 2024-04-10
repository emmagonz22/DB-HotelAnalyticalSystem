from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation
class EmployeeDAO(BaseDAO):
    def validateData(self, json, action):
            try:
                eid = None
                if action == "UPDATE":
                    eid = json["eid"]
                elif action == "CREATE":
                    eid = 1
                hid = json["hid"]
                fname = json["fname"]
                lname = json["lname"]
                age = json["age"]
                position = json["position"]
                salary = json["salary"]

                if not (isinstance(eid, int) and isinstance(hid, int) and isinstance(fname, str) and isinstance(lname, str) and isinstance(age, int) and isinstance(position, str) and isinstance(salary, float)):
                    return False
                
                if not (age > 0 and salary > 0):
                    return False
                
                if position == "Regular":
                    return salary >= 18000 and salary < 50000
                elif position == "Supervisor":
                    return salary >= 50000 and salary < 80000
                elif position == "Administrator":
                    return salary >= 50000 and salary <= 120000
                else:
                    return False
            except Exception as e:
                return False

    def getAllEmployee(self):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT eid, hid, fname, lname, age, position, salary from employee;")
        except Exception as e:
            self.conn.rollback()
            self.conn.close()
            return str(e)
        result = []
        for row in cur:
            result.append(dict(zip(["eid", "hid", "fname", "lname", "age", "position", "salary"], row)))
        self.conn.close()
        return result
    
    def getEmployeebyId(self,eid):
        cur = self.conn.cursor()
        try:
            cur.execute("SELECT eid, hid, fname, lname, age, position, salary from employee where eid = %s;", (eid,))
        except Exception as e:
            self.conn.rollback()
            self.conn.close()
            return str(e)

        rows = cur.rowcount
        info = cur.fetchone()
        self.conn.close()
        # Always needed
        if (rows == 0):
            return "Employee " + str(eid) + " does not exist!"
        result = dict(zip(["eid", "hid", "fname", "lname", "age", "position", "salary"], info))
        return result
    
    def createEmployee(self, json):
        # Validation of data always needed
        if not self.validateData(json, "CREATE"):
            return "Invalid Parameters have been passed!"
        cur = self.conn.cursor()
        data = None
        while(True):
            try:
                cur.execute("INSERT INTO employee(hid, fname, lname, age, position, salary) values (%s, %s, %s, %s, %s, %s) returning eid;",
                            (json["hid"], json["fname"], json["lname"], json["age"], json["position"], json["salary"],))
                data = cur.fetchone()[0]
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
        result = dict(zip(["eid", "hid", "fname", "lname", "age", "position", "salary"], 
                          (data, json["hid"], json["fname"], json["lname"], json["age"], json["position"], json["salary"])))
        self.conn.commit()
        self.conn.close()
        return result

    def deleteEmployeebyId(self,eid):
        cur = self.conn.cursor()
        try:
            cur.execute("DELETE FROM employee where eid = %s;", (eid,))
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
            return "Employee " + str(eid) + " does not exist!"
        return "Deleted " + str(eid)
    
    def updateEmployeebyId(self, json):
        if not self.validateData(json, "UPDATE"):
            return "Invalid parameters have been passed!"
        cur = self.conn.cursor()
        try:
            cur.execute("UPDATE employee SET hid = %s, fname =%s, lname =%s, age =%s, position=%s, salary=%s WHERE eid = %s;",
                                (json["hid"], json["fname"], json["lname"], json["age"], json["position"], json["salary"], json["eid"],))
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
            return "Employee " + str(json["eid"]) + " does not exist!"
        return "Updated " + str(json["eid"])