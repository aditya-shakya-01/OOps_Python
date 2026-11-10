
# Product And Seller

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def showInfo(self,sell):
        print(f"Product Name : {self.name}")
        print(f"Product Price : {self.price}")
        print(f"Seller Name : {sell.name}")
        print(f"Shop Name : {sell.shop_name}")

class Seller:
    def __init__(self,name,shop_name):
        self.name=name
        self.shop_name=shop_name

sell=Seller("Michel","Animation Dump")
product=Product("AK47","9999 $")

product.showInfo(sell)
