
# Bank System...

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, holder_name, acc_no, balance):
        self.holder_name = holder_name
        self._acc_no = acc_no
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    @abstractmethod
    def withdrawal(self, amount):
        pass

    def _withdraw(self, amount):
        if isinstance(amount, (int, float)) and 0 < amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        print("Invalid Amount")
        return None

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.__balance += amount
            print(f"Deposited amount: {amount}")
            return self.__balance
        print("Invalid Amount")
        return None

class SavingsAccount(BankAccount):
    def __init__(self, name, acc_no, balance):
        super().__init__(name, acc_no, balance)

    def withdrawal(self,amount):
        return self._withdraw(amount)

class CurrentAccount(BankAccount):
    def __init__(self, name, acc_no, balance):
        super().__init__(name, acc_no, balance)

    def withdrawal(self,amount):
        return self._withdraw(amount)

savings = SavingsAccount("Aditya", "SA001", 50000)
savings.deposit(2000)
print(savings.withdrawal(5000))

current = CurrentAccount("Krapansh", "CA001", 55000)
print(current.withdrawal(6000))
