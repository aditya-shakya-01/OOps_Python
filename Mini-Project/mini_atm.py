# =====================================
#         Bank Account
# =====================================
import os
import json
from abc import ABC,abstractmethod

class Bank(ABC):
    bank_name="State Bank Of India"
    def __init__(self,form):
        self.form=form

    @ abstractmethod
    def check_balance(self):
        pass

    @ abstractmethod 
    def deposit(self):
        pass

    @ abstractmethod
    def withdrawal(self):
        pass


    def user_detalis(self):
        print("="*30)
        print(f"Bank Name : {self.bank_name}")
        print(f"Account Holder Name : {self.form.holder_name}")
        print(f"Mobile Number : {self.form.mobile_number}")
        print(f"Aadhar Card Number : {self.form.aadhar_number}")
        print(f"Initial Balance : {self.form.initial_balance}")
        print(f"Your Atm Pin : {self.form.pin}")

    def save_json(self,filename="user_data.json"):
        account_data={
            "Bank Name":self.bank_name,
            "Account Holder Name":self.form.holder_name,
            "Mobile Number":self.form.mobile_number,
            "Aadhar Card Number":self.form.aadhar_number,
            "Initial Balance":self.form.initial_balance,
            "Atm Pin":self.form.pin

        }
      
        if os.path.exists(filename):
            try:
                with open(filename,"r") as file:
                    data=json.load(file)

            except Exception as data:
                data=[]
        else:
            data=[]

        data.append(account_data)

        try:
            with open(filename,"w") as file:
        
                json.dump(data,file,indent=4)

        except Exception as e:
            print(e)


class ATM(Bank):
    
    def check_balance(self):
        print("..........Check Balance Services (ATM).........")
        pin=int(input("Enter Your Pin :"))
        if pin==self.form.pin:

            print(f"Your Current Bank Balance : {self.form.initial_balance}")

        else:
            print(f"Wrong Pin ! Please Try Again Later...")

    def deposit(self):
        print("...........Deposit Services (ATM)............")
        amount=int(input("Enter your Amount :"))
        pin=int(input("Enter Your Pin :"))
        if pin==self.form.pin:
            if amount>0:
                self.form.initial_balance+=amount

            else:
                print("Invaild Number ! Please Enter a Valid Number...")
        else:
            print("Wrong Pin ! Please Try Again Later...")


    def withdrawal(self):
        print("...........Withdrawal Services (ATM).............")
        amount=int(input("Enter Your Amount :"))
        pin=int(input("Enter Your Pin :"))
        if pin==self.form.pin:
            if amount<=self.form.initial_balance:
                self.form.initial_balance-=amount

            else:
                print(f"Insuffieciant Balance")

        else:
            print(f"Wrong Pin ! Please Try Again...")

class UPI(Bank):
    def check_balance(self):
        print("..........Check Balance Services (UPI)..........")
        pin=int(input("Enter Your Pin :"))
        if pin==self.form.pin:
            print(f"Your Current Balance : {self.form.initial_balance}")

        else:
            print("Wrong Pin ! Please Try Again Later...")

    def deposit(self):
        print(".........Deposit Services (UPI).........")
        amount=int(input("Enter Your Amount :"))
        pin=int(input("Enter Your Pin :"))

        if pin==self.form.pin:
            self.form.initial_balance+=amount

        else:
            print("Wrong Pin ! Please Try Again Later...")

    def withdrawal(self):
        print("...........Withdrawal Services (UPI).............")
        amount=int(input("Enter Your Amount :"))
        pin=int(input("Enter Your Pin :"))
        if pin==self.form.pin:
            if amount<=self.form.initial_balance:
                self.form.initial_balance-=amount

            else:
                print("Invaild Amount ! Please Enter a valid Amount...")

        else:
            print("Wrong Pin ! Please Try Again Later...")
class Form:
    def __init__(self,holder_name,mobile_number,aadhar_number,initial_balance,pin):
        self.holder_name=holder_name
        self.mobile_number=mobile_number
        self.aadhar_number=aadhar_number
        self.initial_balance=initial_balance
        self.pin=pin

# Object Creation
form=[
    Form("Aditya Shakya",9627209265,967475171054,100,1212),
    Form("Abhinav",9760402062,101010101010,200,1212),
    Form("Krapansh",9595959595,323232323232,300,1212),
    Form("Aseesh",1212121212,989898989898,200,1212)
    ]
for form_data in form:
    bank=Bank(form_data)
    bank.user_detalis()
    bank.save_json()

atm=ATM(form[2])
atm.check_balance()

