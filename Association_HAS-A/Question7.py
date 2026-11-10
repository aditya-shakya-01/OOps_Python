
# Player And Team

class Player:
    def __init__(self,name,jersey_number):
        self.name=name
        self.jersey_number=jersey_number

    def player_details(self,name):
        print(f"Player Name : {self.name}")
        print(f"Jersey Number : {self.jersey_number}")
        print(f"Team Name : {team.name}")


class Team:
    def __init__(self,name):
        self.name=name

team=Team("India")
player=Player("Aditya Shakya",11)

player.player_details(team)