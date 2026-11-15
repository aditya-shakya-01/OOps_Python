# import admin.json
from . import cli
import json
class Bank:

    def admin(self,username,password):
        with open("admin.json","r") as f:
            data=json.load(f)
            if cli.admin==data["user_id"] and cli.password==data["password"]:
                return self.admin

