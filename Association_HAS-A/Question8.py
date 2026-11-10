
# Author And Book 

class Author:
    def __init__(self,name,country):
        self.name=name
        self.country=country

class Book:
    def __init__(self,title,price):
        self.title=title
        self.price=price

    def showInfo(self,auth):
        print(f"Title Name : {self.title}")
        print(f"Price : {self.price}")
        print(f"Author Name : {auth.name}")
        print(f"Country : {auth.country}")

auth=Author("Tulsidas","India")
book=Book("SundarKand",299)

book.showInfo(auth)
