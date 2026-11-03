
# Multiple Interitance

# Creates Two Parent Class

class Father:
    def __init__(self,father_name,father_skill):
       self.father_name=father_name
       self.father_skill=father_skill

class Mother:
    def __init__(self, mother_name, mother_skill):
        self.mother_name=mother_name
        self.mother_skill=mother_skill

class Child(Father,Mother):
    def __init__(self, father_name, father_skill, mother_name, mother_skill):
        Father.__init__(self, father_name, father_skill)
        Mother.__init__(self, mother_name, mother_skill)

    def display(self):
        print(f"Father Name : {self.father_name}")
        print(f"Father Skill : {self.father_skill}")
        print(f"Mother Name : {self.mother_name}")
        print(f"Mother Skill : {self.mother_skill}")

std=Child("Lokesh Kumar","Farmer","Suneeta Devi","HouseWife")
std.display()