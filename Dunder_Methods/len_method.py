
# __len__() method --> len Methods

class Library:
    def __init__(self,books):
        self.books=books

    def __len__(self):
        return len(self.books)

library=Library(["Python","Java","C++"])
print(len(library))