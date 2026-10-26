
# super()---> super() ki help se ham child class ke andar se inheritance chain ke next applicable ko call kar sakte h....

# =================================================
#           Basic Use of Super()
# =================================================

# Create Parent Class 

# class Parent:
#     def __init__(self,name):
#         self.name=name
        
# # Create Child class and child class inherits Form Parent Class

# class Child(Parent):
#     def __init__(self,name,roll_no):
#         super().__init__(name)
#         self.roll_no=roll_no

# # Now we Create object

# obj=Child("Aditya",101)

# print(obj.name)
# print(obj.roll_no)




class Father:
    def show(self):
        print("This is Father Class")
        super().show()

class Mother:
    def show(self):
        print("This is mother Class")
        

class Child(Father,Mother):
    def show(self):
        print("This is Child class")
        super().show()

obj=Child()

obj.show()
