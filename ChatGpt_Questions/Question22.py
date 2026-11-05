
# Food Delivery System

from abc import ABC,abstractmethod
class Delivery(ABC):
    @ abstractmethod
    def calculate_delivery_charge(self):
        pass
    @ abstractmethod
    def estimated_time():
        pass

class BikeDelivery(Delivery):
    def calculate_delivery_charge(self):
        pass

    def estimated_time():
        pass

class TruckDelivery(Delivery):
    def calculate_delivery_charge(self):
        pass

    def estimated_time():
        pass

# Object Creation
bike=BikeDelivery()


truck=TruckDelivery()