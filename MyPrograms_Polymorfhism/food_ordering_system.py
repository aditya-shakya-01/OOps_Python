
# Food Ordering System

class Food:
    def prepare(self):
        print("Food Prepared...")
        

class Pizza(Food):
    def prepare(self):
        super().prepare()
        print("Pizza is Ready...")

class Burger(Food):
    def prepare(self):
        print("Burger is Ready...")

class Pasta(Food):
    def prepare(self):
        print("Pasta is Ready...")
        super().prepare()

pasta=Pasta()
food=Food()

pasta.prepare()
food.prepare()
