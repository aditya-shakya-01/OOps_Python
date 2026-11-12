# ==========================
#    Atm System
# ==========================

class ATM:
    def __init__(self,holder_name,acc_no,balance,mob,pin):
        self.holder_name=holder_name
        self._acc_no=acc_no
        self.__balance=balance
        self._mob=mob
        self.__pin=pin

    
    def check_balance(self):
        print("="*20)
        print("Check Balance Section")
        print("="*20)
        count=1
        while count<=3:
            if count<=3:
                PIN=int(input("Enter Your Pin : "))
                if PIN==self.__pin:
                    print(f"Your Current Balance : {self.__balance}")

                else:
                    count+=1
                    print( f"Incorrect Pin ! Try again later...")

            else:
                
                print( f"Your account have been temporarily block ! Try again after 24 hours...")
                count+=1
                    


    def deposit(self):
        print("="*20)
        print("Deposit Section")
        print("="*20)
        amount=int(input("Enter Your Amount :"))
        PIN=int(input("Enter Your Pin : "))
        if PIN==self.__pin:
            self.__balance+=amount

        else:
            print("Incorrect Pin ! Try again later...")

    def withdrawal(self):
        print("="*20)
        print("Withdrawal Section")
        print("="*20)
        amount=int(input("Enter Your Amount :"))
        PIN=int(input("Enter Your Pin : "))
        if PIN==self.__pin:
            self.__balance-=amount

        else:
            print("Incorrect Pin ! Try again later...")


atm=ATM("Aditya Shakya",1001,55000,9627209265,1212)

(atm.check_balance())
atm.deposit()
(atm.check_balance())
