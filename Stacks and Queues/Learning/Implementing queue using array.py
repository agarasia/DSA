class MyQueue:
    def __init__(self) -> None:
        self.first = -1
        self.currSize = 0
        self.bottom = -1
        self.maxSize = 20
        self.arr = [0] * self.maxSize

    def push(self, data):
        if self.bottom == self.maxSize:
            print("ERROR: Queue is full")
            exit(1)
        if self.bottom == -1:
            self.first = 0
            self.bottom = 0
        else:
            self.bottom = (self.bottom + 1) % self.maxSize
        self.arr[self.bottom] = data
        self.currSize += 1
    
    def pop(self):
        if self.first == -1:
            print("ERROR: Queue is empty")
            exit(1)
        popped = self.arr[self.first]
        if self.currSize == 1:
            self.bottom = -1
            self.first = -1
        else:
            self.first = (self.first + 1) % self.maxSize
        self.currSize -= 1
        return popped
    
    def top(self):
        if self.first == -1:
            print("ERROR: Queue is empty")
            exit(1)
        return self.arr[self.first]
    
    def size(self):
        return self.currSize

q = MyQueue()
q.push(4)
q.push(14)
q.push(24)
q.push(34)
print("The peek of the queue before deleting any element", q.top())
print("The size of the queue before deletion", q.size())
print("The first element to be deleted", q.pop())
print("The peek of the queue after deleting an element", q.top())
print("The size of the queue after deleting an element", q.size())
