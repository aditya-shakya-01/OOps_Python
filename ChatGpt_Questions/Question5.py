
# Bank Account 

class BankAccount:
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance

# Creates Child Classes

class SavingsAccount(BankAccount):
    def __init__(self, holder, balance,interest):
        super().__init__(holder, balance)
        self.interest=interest


    def display(self):
        print("\n...SAVINGS ACCOUNT...\n")
        print(f"Holder Name : {self.holder}")
        print(f"Balance : {self.balance}")
        print(f"With Interest : {(self.balance*4/100)+self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, holder, balance):
        super().__init__(holder, balance)

    def display(self):
        print("...CURRENT ACCOUNT...\n")
        print(f"Holder : {self.holder}")
        print(f"Account Balance : {self.balance}")

# Object Creation 
current=CurrentAccount("Aditya",55000)
current.display()

saving=SavingsAccount("Aditya Shakya",55000,4)
saving.display()