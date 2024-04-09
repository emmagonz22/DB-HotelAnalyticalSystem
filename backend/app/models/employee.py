from .baseDAO import BaseDAO
from psycopg2.errors import UniqueViolation
class EmployeeDAO(BaseDAO):
    def getAllEmployee(self):
        cur = self.conn.cursor()
        cur.execute("SELECT eid, hid, fname, lname, age, position, salary from employee;")
        result = []
        for row in cur:
            result.append(dict(zip(["eid", "hid", "fname", "lname", "age", "position", "salary"], row)))
        self.conn.close()
        return result
    
    def getEmployeebyId(self,eid):
        cur = self.conn.cursor()
        cur.execute("SELECT eid, hid, fname, lname, age, position, salary from employee where eid = %s;", (eid,))
        result = dict(zip(["eid", "hid", "fname", "lname", "age", "position", "salary"], cur.fetchone()))
        self.conn.close()
        return result
    
    def createEmployee(self, json):
        cur = self.conn.cursor()
        data = None
        while(True):
            try:
                cur.execute("INSERT INTO employee(hid, fname, lname, age, position, salary) values (%s, %s, %s, %s, %s, %s) returning eid;",
                            (json["hid"], json["fname"], json["lname"], json["age"], json["position"], json["salary"],))
                data = cur.fetchone()[0]
            except UniqueViolation as e:
                print("Retrying to insert")
            else:
                break
            finally:
                self.conn.commit()
        result = dict(zip(["eid", "hid", "fname", "lname", "age", "position", "salary"], 
                          (data, json["hid"], json["fname"], json["lname"], json["age"], json["position"], json["salary"])))
        self.conn.close()
        return result

    def deleteEmployeebyId(self,eid):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM employee where eid = %s;", (eid,))
        self.conn.commit()
        if (cur.rowcount == 0):
            return ""
        self.conn.close()
        return "Deleted"
    
    def updateEmployeebyId(self, json):
        cur = self.conn.cursor()
        cur.execute("UPDATE employee SET hid = %s, fname =%s, lname =%s, age =%s, position=%s, salary=%s WHERE eid = %s;",
                            (json["hid"], json["fname"], json["lname"], json["age"], json["position"], json["salary"], json["eid"],))
        self.conn.commit()
        self.conn.close()   
        return "Updated"