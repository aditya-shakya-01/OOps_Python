
# Temprature Controller

class Temprature:
    def __init__(self,temprature):
        self.__temprature=temprature

    def set_temprature(self,temprature):
        if -50<=temprature<=55:
            self.__temprature=temprature
            
        else:
            print("Temprature is not found given specific range...")

    def get_temprature(self):
        return f"Current Temprature : {self.__temprature}'C"


# Object Creation

temp=Temprature(30)
print(temp.get_temprature())
# update 
temp.set_temprature(-60)
print(temp.get_temprature())
