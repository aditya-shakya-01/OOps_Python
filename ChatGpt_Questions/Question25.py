
# Banking System

from abc import ABC,abstractmethod
class Account(ABC):
    savings_balance=100000
    current_balance=55000
        
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
        self.savings_balance+=amount
        return f"Your Deposit Amount is {amount}"

    def withdrawal(self,amount):
        self.savings_balance-=amount
        return f"Your Withdrawable Amount is {amount}"

    def calculate_interest(self):
        return f"Your Total Balance With Interest :{(self.savings_balance+self.savings_balance*4/100)}" # 4% Per year Interest

class CurrentAccount(Account):
    
    def deposit(self,amount):
        print("="*20)
        print("Current Account")
        print("="*20)
        self.savings_balance+=amount
        return f"Your Deposit Amount is {amount}"
    
    def withdrawal(self,amount):
        self.savings_balance-=amount
        return f"Your Withdrawable Amount is {amount}"
    
    def calculate_interest(self):
        return f"You must have use Bussiness Account balance {self.current_balance}. Your Account does not support Interest." 

# Object Creation
savings=SavingsAccount()
print(savings.deposit(2000))
print(savings.withdrawal(2000))
print(savings.calculate_interest())

current=CurrentAccount()
print(current.deposit(2000))
print(current.withdrawal(2000))
print(current.calculate_interest())
