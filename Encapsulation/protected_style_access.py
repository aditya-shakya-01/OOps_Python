
# Bank Account

class BankAccount:
    def __init__(self,balance):
        self._balance=balance

    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
        else:
            print("Invaild Balance")

    def get_balance(self):
        return self._balance

acc=BankAccount(10000)
# acc._balance=50000  # Protected Style Attribute modify allow kar deta h lekin convince krta h ki ye protected method h...
acc.deposit(2000)

print(acc.get_balance())