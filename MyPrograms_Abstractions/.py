
# Advanced : Abstract Property

from abc import ABC,abstractmethod

class Person(ABC): # ABC--> Abstract Base Class

    @property
    @abstractmethod
    def name(self):
        pass

# Child Class
class Student(Person):
    def __init__(self,name):
        self._name=name

    @property
    def name(self):
        return self._name

s=Student("Aditya")

print(s.name)