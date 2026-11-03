
# Payment System 

from abc import ABC,abstractmethod

class Payment:
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        return f"Upi Service use : {amount}"

class CardPayment(Payment):
    def pay(self, amount):
        return f"Card Services use : {amount}"

class CashPayment(Payment):
    def pay(self, amount):
        return f"Cash Services Use : {amount}"

# Object Creation 
upi=UPI()
print(upi.pay(2000))

card=CardPayment()
print(card.pay(3000))

cash=CashPayment()
print(cash.pay(5000))