class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self,number):
        self.items.append(number)
    
    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    
stack1 = Stack()
stack1.push(25)
stack1.push(45)
stack1.pop()
stack1.push(99)
stack1.push(78)
stack1.peek()
print(stack1.is_empty())
print(stack1.size())