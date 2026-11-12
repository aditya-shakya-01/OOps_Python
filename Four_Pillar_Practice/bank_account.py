# ===========================
#    Bank Account 
# ===========================

class BankAccunt:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

    def Deposit(self):
        amount=int(input("Enter Your Amount :"))
        self.__balance+=amount
        print(f"Current Balance : {self.__balance} $")

    def withdrawal(self):
        amount=int(input("Enter Your Amount :"))
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Current Balance : {self.__balance} $")
        else:
            print("Insufficent Balance")

bank=BankAccunt("Aditya",56000)
bank.withdrawal()
bank.Deposit()