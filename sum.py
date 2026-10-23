class Solution:
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2

    def sum(self):
        result = [x + y for x, y in zip(self.l1,self.l2)]

        return result

add=Solution([1,2,3],[4,5,6])

print(add.sum())