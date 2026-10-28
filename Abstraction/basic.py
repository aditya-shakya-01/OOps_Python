
# Abstraction in OOPs in Python

from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid Rs. {amount} in using UPI.")

    def show(self,amount):
        print(amount)

class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid Rs. {amount} in using Credit Card.")


upi=UPIPayment()
upi.pay(5000)
upi.show(1000)

card=CreditCardPayment()
card.pay(1000)