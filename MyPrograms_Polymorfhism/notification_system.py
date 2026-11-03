
# Notification System

class Notification:
    def send(self,massage):
        print(f"Notification : {massage}")

class EmailNotification(Notification):
    def send(self,massage):
        print(f"Email Notification : {massage}")

class PushNotification(EmailNotification):
    def send(self,massage):
        super().send("Hii")
        print(f"Push Notification : {massage}")

notify=PushNotification()
notify.send("Hello Guys")
