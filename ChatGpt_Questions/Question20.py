
# Notification System 

from abc import ABC,abstractmethod
class Notification(ABC):
    @ abstractmethod
    def send(self):
        pass

class Email(Notification):
    def send(self):
        print("Email Notification from user...")

class SMS(Notification):
    def send(self):
        print("SMS Notifiaction from user...")

class Whatsapp(Notification):
    def send(self):
        print("Whatsapp Notification from user...")

# Object Creation

email=Email()
email.send()

sms=SMS()
sms.send()

whats=Whatsapp()
whats.send()
