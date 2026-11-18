
# Dependency

# Requirement  ( Payment Processing System)

class PaymentGateway:
    balance=1000
    def deposit_payment(self):
        amount=int(input("Enter Your Amount :"))
        self.balance+=amount

        print(f"Your Current Account Balance : {self.balance}")


class PaymentServices:
    def __init__(self,paymentgateway):
        self.paymentgateway=paymentgateway
        
    def display(self):
        self.paymentgateway.deposit_payment()
payment=PaymentGateway()
pay=PaymentServices(payment)

pay.display()


