# incomplete Question
# E-Wallet
import datetime
class Wallet:
    def __init__(self,user,balance):
        self.user=user
        self.__balance=balance
        self.__transaction=[]

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

            self.__transaction.append(
                f"Deposit Amount : {amount}}"
                
            )

    def withdrawal(self,amount):
        pass

    def transaction_history(self):
        print(self.__transaction)

# Object Creation
usr=Wallet("Aditya Shakya",98000)
usr.deposit(2000)
usr.transaction_history()
