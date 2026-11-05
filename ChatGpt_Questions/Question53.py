
# Password Manager 

class User:
    def __init__(self,username,password):
        self.username=username
        self.__password=password

    def change_pass(self):
        old_pass=input("Enter Your Old Password :")
        if old_pass==self.__password:
            new_pass=input("Enter Your New Password :")
            self.__password=new_pass
            print(f"Password Update Sucessfully...")

        else:
            print("Incorrect Password !")

# Object Creation 
usr=User("adityashakya01","Adityashakya@001")
usr.change_pass()
