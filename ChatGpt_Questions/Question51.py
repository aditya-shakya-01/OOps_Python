
# Product Inventory

class Product:
    def __init__(self,name,stock):
        self.name=name
        self.__stock=stock

    def add_stock(self,quantity):
        if quantity>0:
            self.__stock+=quantity
            # return self.__stock

        else:
            print("Invaild Quantity...")

    def remove_stock(self,quantity):
        if 0<quantity<=self.__stock:
            self.__stock-=quantity
            

        else:
            print("Invalid Quantity ! Please Enter a Valid Number...")

    def details(self):
        return f"Stock : {self.__stock} peice"

# Object Creation

item=Product("Dell XPS 14 Gen...",20)
print(item.details())
# Add Stock 
item.add_stock(7)
print(item.details())
# Remove Stock
item.remove_stock(3)
print(item.details())