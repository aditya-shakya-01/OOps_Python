
# BankAccount

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

        else:
            print("Invaild Amount")

    def get_balance(self):
        return self.__balance


acc=BankAccount(10000)
acc.deposit(2000)

# acc._BankAccount__balance=50000   # Original private attribute internally _BankAccount__balance naam se stored h...

print(acc.get_balance())