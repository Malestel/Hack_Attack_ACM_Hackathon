from flask_login import UserMixin
from . import db 

class User(UserMixin):
    @classmethod
    def get(cls, user_id):

        obj = cls()
        
        try:
            user = db.get_web_user(user_id)
        except KeyError:
            return None

        obj.Name = user['Name']
        obj.id = user['Phone_Number'].encode()
        obj.language = user['Language']
        obj.user_type=user['user_type']

        return obj
    
    def __getitem__(self, key):
        if key == "Name":
            return self.Name

        if key == "Phone_Number":
            return self.id.decode()
        
        if key == "Language":
            return self.language

        if key == "user_type":
            return self.user_type

        raise KeyError(f"Unknown key {key}")

    def keys(self):
        return ("Name", "Phone_Number", "Language", "user_type")


