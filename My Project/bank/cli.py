import services

def admin_menu(bank,admin):
    pass

def run():
    while True:
        print("Press 1 to Admin Login")
        print("Press 2 to Costomer Login")
        print("Press 3 to Atm ")
        print("Press 4 to Exit")
        choice=int(input("Enter Your Choice :"))
        if choice==1:
            admin=admin.admin_login()
            admin_menu(bank,admin)
