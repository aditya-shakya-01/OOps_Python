
# # create two parent class 

class Academic:
    def __init__(self,marks):
        self.marks=marks


    def show_marks(self):
        print(f"My Marks : {self.marks}")

class Sports:
    def __init__(self,sports_score):
        self.sports_score=sports_score

    def show_sports_score(self):
        print(f"My sport Score is : {self.sports_score}")

# Create a child class student 

class Student(Academic,Sports):
    def __init__(self, marks,sports_score):
        Academic.__init__(self,marks)
        Sports.__init__(self,sports_score) # multiple inheritance does not support super() method...

    def total_score(self):
        return f"Total Score is :{self.marks+self.sports_score}"


std=Student(89,91)
std.show_marks()
std.show_sports_score()
print(std.total_score())



        
    