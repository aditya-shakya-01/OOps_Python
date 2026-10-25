
# Hierarchical inheritance In OOPs

class Father:
    def car(self):
        print("Father has a car")

class Son(Father):
    def play(self):
        print("Son is playing")

class Daughter(Father):
    def dance(self):
        print("Daughter is dancing")

# Son object Creating

s=Son()
s.car()
s.play()

# Daughter Object Creating

d=Daughter()
d.car()
d.dance()


