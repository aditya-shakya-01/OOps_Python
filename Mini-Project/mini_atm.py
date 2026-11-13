# =====================================
#      MINI ATM MACHINE PROGRAM
# =====================================

import os
import json

# ==========================
#      Main Bank class
# ==========================

class Bank():
    account_number=10000
    bank_name="State Bank Of India"

    def __init__(self,form):
        self.form=form
        Bank.account_number+=1
        self.account_number=Bank.account_number


    def user_detalis(self):
        print("="*30)
        print(f"Bank Name : {self.bank_name}")
        print(f"Account Holder Name : {self.form.holder_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Mobile Number : {self.form.mobile_number}")
        print(f"Aadhar Card Number : {self.form.aadhar_number}")
        print(f"Initial Balance : {self.form.initial_balance}")
        print(f"Your Atm Pin : {self.form.pin}")

    def save_json(self,filename="user_data.json"):

        account_data={
            "Bank Name":self.bank_name,
            "Account Holder Name":self.form.holder_name,
            "Account Number":self.account_number,
            "Mobile Number":self.form.mobile_number,
            "Aadhar Card Number":self.form.aadhar_number,
            "Initial Balance":self.form.initial_balance,
            "Atm Pin":self.form.pin

        }
        if os.path.exists(filename):
            try:
                with open("user_data.json","r") as file:
                    data=json.load(file)

            except Exception as data:
                data=[]

        else:
            data=[]

        data.append(account_data)

        try:
            with open("user_data.json","w") as file:
                json.dump(data,file,indent=4)

        except Exception as e:
            print(e)

# =============================
#       ATM class
# =============================

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

# ================================
#        UPI class
# ================================

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

# =================================
#    Create a User Delete class
# ================================

class Delete_Users(Bank):
    
    def user_dlt(self):

        # Create a Empty File for contains reaming data after delete user...
        remaining_data=[]

        holder_name=input("Enter Your Name :")
        account_number=int(input("Enter Your Account Number :"))

        with open("user_data.json","r") as file:
            data=json.load(file)
            for row in data:
                if holder_name == row.get("Account Holder Name") and account_number == row.get("Account Number"): # .get() returns the value from keys()
                    
                    with open("Dlt_user.json","w") as file:
                        json.dump(row,file,indent=4)
                                
                    row.clear()
                    print("User Found Successfully ! Delete User Data from database Successfully")
                
                else:
                   remaining_data.append(row)

        with open("user_data.json","w") as file:
            json.dump(remaining_data,file,indent=4)

# ============================
#      Define Exit Method
# ============================

def Exit():
    print("Thanks For Using Our Services ! Welcome Back...")

# ====================================
#         Create Form Class  
# ====================================
        
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
    bank.save_json()



# atm=ATM(form[2])
# atm.check_balance()

while True:
    print("="*30)
    print("Press 1 to Create Accounts")
    print("Press 2 to Transaction")
    print("Press 3 to display Users")
    print("Press 4 to delete Users")
    print("Press 5 to Exit")

    n=int(input("Enter Your Choice ..."))
    if n==1:
        pass

    if n==2:
        pass
    
    if n==3:
        for form_data in form:
            bank=Bank(form_data)
            bank.user_detalis()
            # here some correction data shown by updated json file

    if n==4:
        dlt=Delete_Users(form)
        dlt.user_dlt()

    if n==5:
        Exit()
        break

