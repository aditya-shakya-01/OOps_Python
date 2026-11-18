
# Book and Pages

class Page:
    def __init__(self,page_number,content):
        self.page_number = page_number
        self.content = content

class Book:
    def __init__(self):
        self.book=Page(2000,"Rich and Poor Dad")

    def display(self):
        print(f"Book Name : {self.book.content} and book pages {self.book.page_number}")

# Object Creation

book=Book()
book.display()