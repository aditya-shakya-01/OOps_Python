
# Create a Parent class notificaton

class Notification:
    def send(self):
        print("Sending a General Notification")

# Cereate Two Classes

class EmailNotification(Notification):
    def send(self):
        print("Sending a Email Notifiaction")
        super().send()

# Create Objects

n1=EmailNotification()
n1.send()
