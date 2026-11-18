
# Intermediate Questions

# ATM and Card Reader

class CardReader:
    def __init__(self,reader):
        self.reader=reader


class ATM:
    def __init__(self,cardreader):
        self.cardreader=cardreader
        self.cardReader=CardReader("Done")

    def insert(self):
        pass

    def read(self):
        pass

# Object Creation

atm=ATM()
atm.insert()
atm.read()