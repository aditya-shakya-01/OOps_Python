from services import Bank

while True:
    print("1","Admin Login")
    print("2","Costomer Login")
    print("3","ATM")
    print("$","Exit")

    if n==1:
        admin=input("Enter admin username :")
        password=input("Enter Your Password :")
        Bank.admin()
        break

    n=int(input("Enter Your Choice :"))