
class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def check_balance(self):
        return self.balance

    def deposit(self,amount):
        self.balance+=amount

    def withdrawal(self,amount):
        self.balance-=amount

account=BankAccount(10000)

print(account.check_balance())

account.deposit(2000)

print(account.check_balance())

account.withdrawal(1000)

print(account.check_balance())