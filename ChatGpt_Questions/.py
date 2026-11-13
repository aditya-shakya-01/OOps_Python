import json
import os

class Bank:
    bank_name = "State Bank Of India"
    account_number = 1000

    def __init__(self, form):
        self.form = form
        if self.form.initial_bal <= 100:
            raise ValueError("Your Initial Balance is Less Or Equal to 100...")

        Bank.account_number += 1
        self.account_numbers = Bank.account_number

        # Save details to JSON whenever an account is successfully created
        self.save_to_json()

    def user_datails(self):
        print("=" * 30)
        print(f"Bank Name : {self.bank_name}")
        print("=" * 30)
        print(f"Account Holder Name : {self.form.holder_name}")
        print(f"Account Number : {self.account_numbers}")
        print(f"Mobile Number : {self.form.mobile_num}")
        print(f"Aadhar Number : {self.form.aadhar_card}")
        print(f"Initial Balance : {self.form.initial_bal} $")

    def save_to_json(self, filename="bank_accounts.json"):
        account_data = {
            "bank_name": self.bank_name,
            "account_number": self.account_numbers,
            "holder_name": self.form.holder_name,
            "mobile_num": self.form.mobile_num,
            "aadhar_card": str(self.form.aadhar_card),
            "initial_bal": self.form.initial_bal
        }

        # Load existing data if the file exists, otherwise start a new list
        if os.path.exists(filename):
            try:
                with open(filename, "r") as file:
                    data = json.load(file)
                if not isinstance(data, list):
                    data = []
            except (json.JSONDecodeError, OSError):
                data = []
        else:
            data = []

        # Append new account details and save back to file
        data.append(account_data)
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

class Form:
    def __init__(self, holder_name, mobile_num, aadhar_card, initial_bal):
        self.holder_name = holder_name
        self.mobile_num = mobile_num
        self.aadhar_card = aadhar_card
        self.initial_bal = initial_bal

forms = [
    Form("Aditya Shakya", 962720965, "1234-5678-9012", 1000),
    Form("Abhinav", 9760402062, "9876-5432-1098", 200)
]

try:
    for form in forms:
        bank = Bank(form)
        bank.user_datails()
except Exception as e:
    print(e)