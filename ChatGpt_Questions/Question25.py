
# Banking System

from abc import ABC,abstractmethod
class Account(ABC):
    balance=100000
        
    @ abstractmethod
    def deposit(self):
        pass
    @ abstractmethod
    def withdrawal(self):
        pass
    @ abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    
    def deposit(self,amount):
        print("="*20)
        print("Savings Account")
        print("="*20)
        self.balance+=amount
        return f"Your Deposit Amount is {amount}"

    def withdrawal(self,amount):
        self.balance-=amount
        return f"Your Withdrawable Amount is {amount}"

    def calculate_interest(self):
        return f"Your Total Balance With Interest :{(self.balance+self.balance*4/100)}" # 4% Per year Interest

class CurrentAccount(Account):
    
    def deposit(self,amount):
        print("="*20)
        print("Current Account")
        print("="*20)
        self.balance+=amount
        return f"Your Deposit Amount is {amount}"
    
    def withdrawal(self,amount):
        self.balance-=amount
        return f"Your Withdrawable Amount is {amount}"
    
    def calculate_interest(self):
        return f"You must have use Bussiness Account balance {self.balance}. Your Account does not support Interest." 

# Object Creation
savings=SavingsAccount()
print(savings.deposit(2000))
print(savings.withdrawal(2000))
print(savings.calculate_interest())

current=CurrentAccount()
print(current.deposit(2000))
print(current.withdrawal(2000))
print(current.calculate_interest())
