# ==========================
#    Atm System
# ==========================

from abc import ABC,abstractmethod
class Bank(ABC):
    def __init__(self,holder_name,acc_no,balance,mob,pin):
        self.holder_name=holder_name
        self._acc_no=acc_no
        self.__balance=balance
        self._mob=mob
        self.__pin=pin

    @ abstractmethod
    def check_balance(self):
        pass

    @ abstractmethod
    def deposit(self):
        pass

    @ abstractmethod
    def withdrawal(self):
        pass

class ATM(Bank):
    def __init__(self,bank):
        self.bank=bank
    
    def check_balance(self):
        pass


    def deposit(self):
        print("="*20)
        print("Deposit Section")
        print("="*20)
        amount=int(input("Enter Your Amount :"))
        PIN=int(input("Enter Your Pin : "))
        if PIN==self._Bank__pin:
            self.__balance+=amount

        else:
            print("Incorrect Pin ! Try again later...")

    def withdrawal(self):
        print("="*20)
        print("Withdrawal Section")
        print("="*20)
        amount=int(input("Enter Your Amount :"))
        PIN=int(input("Enter Your Pin : "))
        if PIN==self.bank.__pin:
            self.__balance-=amount

        else:
            print("Incorrect Pin ! Try again later...")



bank=("Aditya Shakya",1001,55000,9627209265,1212)

atm=ATM(bank)

atm.deposit()
