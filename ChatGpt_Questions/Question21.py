
# DataBase Connection

from abc import ABC,abstractmethod
class DataBase(ABC):
    @ abstractmethod
    def connect(self):
        pass
    @ abstractmethod
    def disconnect(self):
        pass

# Create Child Classes

class MySQL(DataBase):
    def connect(self):
        print("MySQL is connected to DataBase...")

    def disconnect(self):
        print("MySQL is disconneted to DataBase...")

class PostgreSQL(DataBase):
    def connect(self):
        print("PostgreSQL is connected to DataBase...")

    def disconnect(self):
        print("PostgreSQL is disconnected to DataBase...")

# Object Creation

my=MySQL()
my.connect()
my.disconnect()

post=PostgreSQL()
post.connect()
post.disconnect()