
# Payment System

from abc import ABC,abstractmethod
class Payment(ABC):
    @ abstractmethod
    def pay(self):
        pass

class UPIPayment(Payment):
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        return f"Pay {self.amount} using UPI..."

class CreditPayment(Payment):
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        return f"Pay {self.amount} using Credit..."

class CashPayment(Payment):
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        return f"Pay {self.amount} using Cash..."

# Object Creation

upi=UPIPayment(2000)
print(upi.pay())

credit=CreditPayment(3000)
print(credit.pay())

cash=CashPayment(5000)
print(cash.pay())