
# User And Profile

class User:
    def __init__(self,username,email):
        self._username=username
        self._email=email

    def details(self,profile):
        print(f"Username : {self._username}")
        print(f"Email Id : {self._email}")
        print(f"Bio : {profile.bio}")
        print(f"Profile Picture : {profile.picture}")

class Profile:
    def __init__(self,bio,picture):
        self.bio=bio
        self.picture=picture

profile=Profile("Hard Working Man","No Profile Picture")
user=User("adityashakya01","adityashakya0721@gmail.com")

user.details(profile)