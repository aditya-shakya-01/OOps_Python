
# Payment System 

class Payment:
    def pay(self):
        pass

class UPIPayment(Payment):
    def pay(self,amount):
        return f"UPI Pay :{amount}"

class CardPayment(Payment):
    def pay(self,amount):
        return f"Card Pay :{amount}"

class CashPayment(Payment):
    def pay(self,amount):
        return f"Cash Pay :{amount}"

# Object Creation 

upi=UPIPayment()
card=CardPayment()
cash=CashPayment()

print(upi.pay(2000))
print(card.pay(5000))
print(cash.pay(10000))