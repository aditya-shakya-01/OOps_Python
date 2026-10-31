
# Smart phone System in OOPs Programming in Python

# Create two parent class 

class Camera:
    def take_photo(self):
        print("Photo Captured...")

class MusicPlayer:
    def play_music(self):
        print("Playing Music...")

# Create a Child Class 

class SmartPhone(Camera,MusicPlayer): # Multiple Inheritance...
    def __init__(self,brand):
        self.brand=brand

    def display(self):
        print("Brand's Name :",self.brand)

obj=SmartPhone("iPhone18 Pro Max")

obj.display()
obj.take_photo()
obj.play_music()
        