# my_balance=10000
Atm_PIN=1212
class Bank:
    def __init__(self,bank_name):
        self.bank_name=bank_name

class Users(Bank):
    def __init__(self, bank_name,branch_code,user_name,acc_no,initial_balance):
        super().__init__(bank_name)
        self.user_name=user_name
        self.acc_no=acc_no
        self.branch_code=branch_code
        self.initial_balance=initial_balance

    def Display_Users(self):
        print("="*30)
        print("Bank Name :",self.bank_name)
        print("Branch Code :",self.branch_code)
        print("Account Holder Name :",self.user_name)
        print("User's Account No :",self.acc_no)
        print("Initial Balance :",self.initial_balance)

class Atm:
    def __init__(self,user_mine,initial_bal):
        self.user_mine=user_mine
        self.initial_bal=initial_bal
    def deposit(self):
        print("="*20)
        print("USING ATM SERVICES")
        print("-"*25)
        print("You choose Deposit Section")
        print("-"*25)
        print("="*20)
        amount=int(input("Enter Amount For Deposit :"))
        pin=int(input("Enter Your Pin :"))
        if pin==Atm_PIN:
            
            initial_bal=self.initial_bal.initial_balance
            initial_bal+=amount
            my_balance=initial_bal
            print(f"Your Deposit Amount {amount} and your balance {my_balance}.")
            print(f"Welcome back {self.user_mine.user_name} Thanks For USing Our Services, Have a nice day.")
        else:
            print("Wrong Pin Please Enter a Valid Pin.")

    def withdrawal(self,amount):
        pin=int(input("Enter Your Pin :"))
        if pin==Atm_PIN:
            global my_balance
            my_balance-=amount
            print(f"Your Withdrawal Amount {amount} Using Atm Services.")

    def check_balance(self):
        pin=int(input("Enter Your Pin :"))
        if pin==Atm_PIN:
            print(f"Your Current Account Balance : {my_balance}")

class Upi:
    def deposit(self,amount):
        global my_balance
        my_balance+=amount
        print(f"Your Deposit Amount {amount} Using UPI Services.")
    
    def withdrawal(self,amount):
        global my_balance
        my_balance-=amount
        print(f"Your Withdrawal Amount {amount} Using Atm Services.")
    
    def check_balance(self):
        print(f"Your Current Account Balance : {my_balance}")


# user1=Atm("sbi","adi",123456,"sbin2021")
user2=[
    Users("SBI","SBIN2012","Aditya Shakya",123456,1000),
    Users("HDFC","HDFC2012","Krapansh",909090,2000),
    Users("PNB","PNB2012","Abhinav",123123,3000),
    Users("ICICI","ICICI2012","Aseesh",2323323,1500),
    Users("BOB","BOB2012","Anshul",455545,2500)
    
]

count=0
for user in user2:
    user.Display_Users()
    user_atm=Atm(user)
    user_atm.deposit()
    count+=1
    if count==2:
        break



