
# Bank Account

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def get_balance(self):
        return self.__balance

    def set_balance(self,amount):
        if amount>0:
            self.__balance=amount

        else:
            raise Exception("Please Enter a valid Amount...")
        
# Create Object
account=BankAccount("Aditya Shakya",55000)
# Get Balance
print(account.get_balance())
# Set Balance
account.set_balance(20000)
# Get Balance
print(account.get_balance())