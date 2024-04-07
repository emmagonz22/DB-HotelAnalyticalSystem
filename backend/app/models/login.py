import json

class Login:
    def __init__(self, 
                lid, 
                eid,
                username, 
                password):
        self.lid = lid
        self.eid = eid
        self.username = username
        self.password = password

    # Map JSON string to Login object
    @classmethod
    def create_login(cls, json_string):

        if not json_string:
            return None

        json_object = json.codec

    

