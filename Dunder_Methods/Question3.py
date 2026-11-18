
# Custom Length

class Team:
    def __init__(self,member):
        self.member=member


    def __len__(self):
        return len(self.member)

team=Team(["Aditya","Ashish","Abhinav","Krapansh"])

print(len(team))

