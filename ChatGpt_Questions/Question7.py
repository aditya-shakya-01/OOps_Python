
# MultiLevel Inheritance

class GrandFather:
    def __init__(self,grand_skill):
        self.grand_skill=grand_skill

class Father(GrandFather):
    def __init__(self, grand_skill,father_skill):
        super().__init__(grand_skill)
        self.father_skill=father_skill

class Child(Father):
    def __init__(self, grand_skill, father_skill,child_skill):
        super().__init__(grand_skill, father_skill)
        self.child_skill=child_skill

    def display_skill(self):
        print(f"Grand Father Skill : {self.grand_skill}")
        print(f"Father Skill : {self.father_skill}")
        print(f"Children's Skill : {self.child_skill}")


# Object Creation 
std=Child("Figher","Farmer","Coder")

std.display_skill()