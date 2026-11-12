# =====================================
#      Online Payment System 
# =====================================

from abc import ABC,abstractmethod

class Payment(ABC):

    @abstractmethod

    def Payment(self):
        pass

class UPIPayment(Payment):
    def __init__(self,amount):
        self.amount=amount

    def Payment(self):
        return f"You choice upi method and your payable amount : {self.amount}"

class CardPayment(Payment):
    def __init__(self,amount):
        self.amount=amount

    def Payment(self):
        return f"You choice card method and your payable amount : {self.amount}"

class WalletPayment(Payment):
    def __init__(self,amount):
        self.amount=amount

    def Payment(self):
        return f"You choice wallet method and my payable amount : {self.amount}"

# Object Creation 

upi=UPIPayment(2000)
card=CardPayment(3000)
wallet=WalletPayment(5000)


print(upi.Payment())
print(card.Payment())
print(wallet.Payment())

