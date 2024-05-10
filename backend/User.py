from app.controller.employee import BaseEmployee
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self,user_dict):
        print(user_dict)
        self.lid = user_dict.get("lid")
        self.eid = user_dict.get("eid") 
        self.username = user_dict.get("username")
        self.password_hash = user_dict.get("password")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_employee(self):
        return BaseEmployee().getEmployeebyId(self.eid)

    def get_id(self):
        return self.lid

    @staticmethod
    def get_employee_by_Id(eid):
        return BaseEmployee().getEmployeebyId(eid)


    def __str__(self):
        return f'User: {self.username}'


