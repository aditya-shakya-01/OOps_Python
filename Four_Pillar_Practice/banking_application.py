# ==============================
#    Banking Application
# ==============================

import datetime
from abc import ABC , abstractmethod

class BankAccount(ABC):
    def __init__(self,holder_name,mob,acc_no,balance):
        self.holder_name=holder_name
        self.mob=mob
        self.acc_no=acc_no
        self.__balance=balance
    
    def get_balance(self):
        return self.__balance

    # @ abstractmethod
    # def deposit(self):
    #     pass

class SavingsAccount(BankAccount):
    def __init__(self, holder_name, mob, acc_no, balance):
        super().__init__(holder_name, mob, acc_no, balance)

    def withdrawal(self):
        amount=int(input("Enter your amount :"))
        _BankAccount__balance-=amount

    def transaction_history(self):
        pass

    def transfer(self):
        pass

class CurrentAccount(BankAccount):
    def __init__(self):
        pass

    def withdrawal(self):
        pass

    def transaction_history(self):
        pass

    def transfer(self):
        pass

bank=BankAccount("Aditya Shakya",9627209265,1001,55000)
savings=SavingsAccount("Aditya Shakya",9627209265,1001,55000)
savings.withdrawal()
