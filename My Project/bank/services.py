from .config import ADMIN_USERNAME,ADMIN_PASSWORD

class Bank:
    def __init__(self):
        pass


    def admin_login(self,username,password):
        if username==ADMIN_USERNAME and password==ADMIN_PASSWORD:
            return self.admin_login