from app.controller.employee import BaseEmployee
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, eid):
        self.eid = eid

    def get_employee(self):
        return BaseEmployee().getEmployeebyId(self.eid)

    def get_id(self):
        return self.eid

    @staticmethod
    def get(self, eid):
        return User(eid)
        
    @staticmethod
    def get_employee_by_Id(eid):
        return BaseEmployee().getEmployeebyId(eid)

    def __str__(self):
        return f'{self.eid}'


