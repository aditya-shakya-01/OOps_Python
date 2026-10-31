
# Create Parent class BankAccount
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    # Method deposit(amount) to add money to the balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"Diposited : {amount}")

    # Method show_balance() to display the balance
    def show_balance(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Current Balance : {self.balance}")
        

# Create a Child class SavingsAccount and Inherits BankAccount
class SavingsAccount(BankAccount):
    # Attribute Interest Rate
    def __init__(self, account_holder, balance, interest_rate):
        self.interest_rate=interest_rate
        super().__init__(account_holder, balance)

    # Method calculate_interest() that returns the imterest for one year
    def calculate_interest(self):
        return f"Interest for one year: {self.balance*self.interest_rate/100}"
    
# Creating Object

obj=SavingsAccount("Aditya",10000,5)
obj.show_balance()
obj.deposit(2000)
print(obj.calculate_interest())
