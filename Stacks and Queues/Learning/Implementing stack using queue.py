import queue

class myStack:
    def __init__(self) -> None:
        self.queue = queue.Queue()
    
    def push(self, newData):
        size = self.queue.qsize()
        self.queue.put(newData)
        for i in range(size):
            self.queue.put(self.queue.get())

    def pop(self):
        n = self.queue.get()
        return n
    
    def top(self):
        return self.queue.queue[0]
    
    def size(self):
        return self.queue.qsize()
    
s = myStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print("Top of the stack: ", s.top())
print("Size of the stack before removing element: ", s.size())
print("The deleted element is: ", s.pop())
print("Top of the stack after removing element: ", s.top())
print("Size of the stack after removing element: ", s.size())