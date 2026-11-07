
# File Processing System

from abc import ABC,abstractmethod
class FileProcessor(ABC):
    @ abstractmethod
    def read_file(self):
        pass

    @ abstractmethod
    def process_file(self):
        pass

class CSVProcessor(FileProcessor):
    def read_file(self):
        import csv
        with open("std.csv","r") as file:
            data=csv.DictReader(file)
            return data
           
            
    def process_file(self):
        data=self.read_file()
        # print(data)
        for row in data:
            if int(row["marks"])>70:
                print(row)

class JSONProcessor(FileProcessor):
    pass

# Object Creation
csv=CSVProcessor()
csv.read_file()
csv.process_file()