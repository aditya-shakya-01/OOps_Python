
# Authentication System

from abc import ABC,abstractmethod

class Authentication(ABC):
    @ abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class PasswordAuth(Authentication):
    def __init__(self,username,password):
        self.username=username
        self.__password=password

    def login(self):
        user=input("Enter Your username :")
        if user==self.username:
            user_pass=input("Enter Your Password :")
            if user_pass==self.__password:
                print(f"Welcome User , GO on Dashboard...")

            else:
                print(f"Incorrect Password ! Please Enter Your Password...")

        else:
            print(f"User not Found ! ")

    def logout(self):
        user_pass=input("Enter Your Password :")
        if user_pass==self.__password:
            print(f"Logout Successfully ! Have a Nice Day...")

class OTPAuth(Authentication):
    def __init__(self,phone_number,otp):
        self.phone_number=phone_number
        self.__otp=otp

    def login(self):
        phone=int(input("Enter Your Phone Number :"))
        if phone==self.phone_number:
            user_otp=int(input("Enter Your OTP :"))
            if user_otp==self.__otp:
                print(f"Login Successfully ! Welcome to Bashboard...")
            else:
                print(f"Incorrect OTP ! Please Enter Your Otp...")

        else:
            print(f"Account Not Found ! Try Again Later...")
    def logout(self):
        user_otp=int(input("Enter Your Otp :"))
        if user_otp==self.__otp:
            print(f"Logout Successfully ! Welcome Back User...")
        else:
            print(f"OTP Invaild ! Please Enter Your OTP...")
# Object Creation

password=PasswordAuth("adityashakya01","Aditya@123")
password.login()
password.logout()

otp=OTPAuth(9627209265,1991)
otp.login()
otp.logout()