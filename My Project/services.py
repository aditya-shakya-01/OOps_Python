from . import config

class Bank:
    def __init__(self):
        pass


    def admin_login(self,username,password):
        if username=="admin" and password=="admin123":
            return self.admin_login