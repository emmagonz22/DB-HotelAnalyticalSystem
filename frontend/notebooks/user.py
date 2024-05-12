class User():

    def __init__(self, user_info={'username':'', 'eid':'', 'hid':'', 'fname':'', 'lname': '', 'age':'', 'position':'', 'salary':''}):
        """Initializes user with given data."""
        self.username = user_info['username']
        self.eid = user_info['eid']
        self.hid = user_info['hid']
        self.fname = user_info['fname']
        self.lname = user_info['lname'] 
        self.age = user_info['age']
        self.position = user_info['position']
        self.salary = user_info['salary']
        self.all = user_info

    def is_authenticated(self):
        return self.username != ''

    def get_eid(self):
        return self.eid
    
    def get_hid(self):
        return self.hid
    
    def get_all(self):
        return self.all
    
    def get_position(self):
        return self.position
    
    def logout(self):
        user_info={'username':'', 'eid':'', 'hid':'', 'fname':'', 'lname': '', 'age':'', 'position':'', 'salary':''}
        self.username = user_info['username']
        self.eid = user_info['eid']
        self.hid = user_info['hid']
        self.fname = user_info['fname']
        self.lname = user_info['lname'] 
        self.age = user_info['age']
        self.position = user_info['position']
        self.salary = user_info['salary']
        self.all = user_info


user_login = User()