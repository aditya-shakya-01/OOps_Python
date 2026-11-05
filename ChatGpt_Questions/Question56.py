
# Secure Banking System

class BankAccount:
    def __init__(self,name,acc_first,balance):
        self.name=name
        self._acc_first=acc_first
        self.__balance=balance
        self.__pin=1001

    def deposit(self,amount):
        pin=int(input("Enter Your Pin :"))
        if pin==self.__pin:
            if amount>0:
                self.__balance+=amount

            else:
                print("Invaild Amount")
        else:
            print("Incorrect Pin ! Please Enter your pin...")
        
    

    def withdrawal(self,amount):
        pin=int(input("Enter Your Pin :"))
        if pin==self.__pin:
            if 0<amount<=self.__balance:
                self.__balance-=amount

            else:
                print("Insufficient Balance...")

        else:
            print("Incorrect Pin ! Please Enter Your Pin...")

    def transfer(self,acc_no):
        amount=int(input("Enter Your Amount :"))
        if 0<amount:
            pin=int(input("Enter Your Pin :"))
            if pin==self.__pin:
                if amount<=self.__balance:
                    self.__balance-=amount
                else:
                    print("Insuffecint Balance...")
            else:
                print("Wrong Pin ! Please Enter Your Pin")

        else:
            print("Invaild Amount...")
        


# Object Creation 

acc=[BankAccount("Aditya Shakya",10000001,98000),BankAccount("Adi",10000002,55000)]
for i in acc:
    print(i._acc_first)
    if 10000001 in acc[1]:
        print("yes")
    else:
        print("No")
