class myQueue:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def push(self, data):
        # Stack 1 to Stack 2
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        # Appending to stack 1
        self.stack1.append(data)

        # Stack 2 to Stack 1
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self):
        return self.stack1.pop()
    
    def peek(self):
        return self.stack1[-1]
    
    def empty(self):
        return len(self.stack1) == 0
    

q = myQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.peek())
print(q.stack1)
print(q.pop())
print(q.stack1)
print(q.empty())