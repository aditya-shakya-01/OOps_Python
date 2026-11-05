
# Banking Management System

# Create a banking system with different account types.

# Requirements:
# - Create abstract class BankAccount.
# - Store __balance privately.
# - Create deposit() and withdraw() methods.
# - Create SavingsAccount and CurrentAccount.
# - Override withdraw() in both child classes.
# - Savings account must maintain minimum balance.
# - Current account must support overdraft limit.
# # - Create get_balance() to access balance safely.

from abc import ABC,abstractmethod

class BankAccount(ABC):
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def Deposit(self,amount):
        if amount<=0:
            raise Exception("Please Enter a Valid Amount...")
        self.__balance+=amount
        return  self.__balance

    def withdrawal(self,amount):
        self.__balance-=amount
        return self.__balance

    @ abstractmethod
    def withdrawal(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def withdrawal(self,amount):
        pass
savings=SavingsAccount("Aditya",10000)
savings.Deposit(2000)
print(savings.get_balance())
savings.withdrawal(5000)
print(savings.get_balance())