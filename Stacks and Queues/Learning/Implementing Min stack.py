# Implement a stack with additional feature
# to get the minimum element in constant time.
class myMinStack:
    def __init__(self) -> None:
        self.arr = []
        self.min = float('inf')
        self.min2 = float('inf')

    def push(self, data):
        self.arr.append(data)
        self.min = min(self.min, self.arr[-1])
    
    def pop(self):
        return self.arr.pop()
    
    def top(self):
        return self.arr[-1]
    
    def getMin(self):
        return self.min
    