
# Product Addition

class Product:
    def __init__(self,price):
        self.price=price
        

# Implimemt __add__() method
    def __add__(self, other):
        return (f"Total Price : {self.price+other.price}")

p1=Product(300)
p2=Product(500)

print(p1+p2)
