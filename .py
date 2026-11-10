
# Object Relationship in OOPs Programming

class Bank:
    bank_name="State Bank Of India"
    account_number=1000

    def __init__(self,form):
        self.form=form
        if self.form.initial_bal<=100:
            raise Exception("Your Initial Balance in Less Or Equal to 100...")
        
        Bank.account_number+=1
        self.account_numbers=Bank.account_number
    def user_datails(self):
        print("="*30)
        print(f"Bank Name : {self.bank_name}")
        print("="*30)
        print(f"Account Holder Name : {self.form.holder_name}")
        print(f"Account Number : {self.account_numbers}")
        print(f"Mobile Number : {self.form.mobile_num}")
        print(f"Aadhar Number : {self.form.aadhar_card}")
        print(f"Initial Balance : {self.form.initial_bal} $")

class Form:
    def __init__(self,holder_name,mobile_num,aadhar_card,initial_bal):
        self.holder_name=holder_name
        self.mobile_num=mobile_num
        self.aadhar_card=aadhar_card
        self.initial_bal=initial_bal

forms=[
    Form("Aditya Shakya",962720965,967475171054,1000),
    Form("Abhinav",9760402062,101010101010,200)
    
    ]
try:
    for form in forms:
        bank=Bank(form)
        bank.user_datails()
except Exception as e:
    print(e)