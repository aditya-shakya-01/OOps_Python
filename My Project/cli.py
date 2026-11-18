from . import ui

from .services import Bank

def admin_menu(bank,admin):
    pass

def admin_create_user(bank):
    ui.banner("Create Costomer Account")

    name=ui.ask("Full Name")
    phone=ui.ask("Mobile No (10 Digits)")
    email = ui.ask("Email")
    password = ui.ask_secret("Set initial password")
    balance = ui.ask_amount("Opening balance (0 for none)")
    bank.send_registration_otp(phone)
    otp = ui.ask("Enter OTP given to customer")
    user = bank.create_user(name, phone, email, password, balance, otp)
    ui.ok("Account created!")
    print(f"  User ID : {user.user_id}\n  Account : {user.account_no}\n  UPI ID  : {user.upi_id}")


def run():
    bank=Bank()

    while True:
        choice=ui.menu("Main Menu",[("1","Admin"),("2","Costomer"),("3","ATM"),("4","EXIT")])

        if choice=="1":
            admin=bank.admin_login(ui.ask("Admin Username"),ui.ask_secret("Admin Password"))

            admin_menu(bank,admin)

