class MyStack:
    def __init__(self) -> None:
        self.nums = []
    
    def push(self, data):
        self.nums.append(data)


    def pop(self):
        if not self.nums:
            return -1
        return self.nums.pop()
    
    def print(self):
        print(self.nums)

# Driver program
stack = MyStack()
print(stack.pop())
stack.push(1)
stack.push(2)
stack.print()
print(stack.pop())
stack.push(3)
stack.print()