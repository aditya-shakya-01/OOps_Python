
# Library Management System 

class Book:
    def __init__(self,name):
        self.name=name
        


class Library:
    def __init__(self):
        self.book_title=Book("Rich And Poor Dad")
        self.book_author=Book("Asheesh Shakya")

    def display(self):
        print(f"Book Title : {self.book_title.name}\nAuthor : {self.book_author.name}")

lib=Library()
lib.display()