
# Atm System 

class Atm:
    def __init__(self,name,pin,balance):
        self.name=name
        self.__pin=pin
        self.__balance=balance

    def deposit(self,amount):
        atm_pin=int(input("Enter Your Pin :"))
        if atm_pin==self.__pin:
            if amount>0:
                self.__balance+=amount
                print(f"Your Deposit  Amount is : {amount}")
                return self.__balance
            else:
                return f"Invalid Amount  ..."
        else:
                return f"Incorrect Pin ! Please Enter Your Pin..."

    def withdrawal(self,amount):
        atm_pin=int(input("Enter Your Pin :"))
        if atm_pin==self.__pin:
            if amount>0 and amount<=self.__balance:
                self.__balance-=amount
                print(f"Your Withdrawable Amount is : {amount}")
                return self.__balance
            else:
                return f"Insufficient Balance ..."
        else:
            return f"Incorrect Pin ! Please Enter Your Pin..."

    def check_balance(self):
        return f"Your Current Balance : {self.__balance}"

# Object Creation

acc=Atm("Aditya Shakya",1909,95000)
print(acc.check_balance())
# Withdrawal Amount
print(acc.withdrawal(20000))
# Deposit Balance
print(acc.deposit(30000))