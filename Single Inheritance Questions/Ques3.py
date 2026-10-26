

# Create a `Person` class with `name` and `age`. Create a `Student` class with an additional `roll_number`. Display all details.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age,roll_no):
        super().__init__(name, age)
        self.roll_no=roll_no

    def showInfo(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Roll No :",self.roll_no)

s1=Student("Aditya",18,101)


s1.showInfo()