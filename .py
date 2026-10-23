
class Account:
    bank="State Bank Of India"
    AccountNumber=1000
    def __init__(self,name,mob,initial_bal):
        if initial_bal<100:
            raise Exception("Should be greter than 100 for creating Account")
        self.name=name
        self.mob=mob
        self.initial_bal=initial_bal
        self.AccountNumber+=1
        self.AccountNumber=Account.AccountNumber

    def ShowInfo(self):
        print("="*30)
        print("Bank Name :",self.bank)
        print("Account Number :",self.AccountNumber)
        print("Account Holder Name :",self.name)
        print("Mob :",self.mob)
        print("Initial Balance :",self.initial_bal)

try: 
    acc1=Account("Aditya",9627209265,2000)
    acc2=Account("Abhinav",9760402062,500)
    acc3=Account("Monty",9520660568,100)
        
except Exception as e:
    print(e)

try:
    acc1.ShowInfo()
    acc2.ShowInfo()
    acc3.ShowInfo()

except Exception as e:
    print(e)