class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

        with open("transactions.txt", "a") as file:
            file.write(f"{self.name} deposited {amount}\n")

    def show_balance(self):
        return self.__balance

    def show_history(self):
        with open("transactions.txt", "r") as file:
            print(file.read())


account = BankAccount("Aditya", 5000)

account.deposit(1000)
account.show_history()