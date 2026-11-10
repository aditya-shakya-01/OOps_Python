
# Costomer And BankAccount 

class Costomer:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone

class BankAccount:
    def __init__(self,acc_num,balance):
        self.__acc_num=acc_num
        self.__balance=balance

    def user_info(self,costomer):
        print(f"User Name : {costomer.name}")
        print(f"Phone Number : {costomer.phone}")
        print(f"Account Number : {self.__acc_num}")
        print(f"Balance : {self.__balance}")

costomer=Costomer("Aditya Shakya",9627209265)
bank=BankAccount(101010101010,98000)

bank.user_info(costomer)