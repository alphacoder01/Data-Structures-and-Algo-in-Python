from stack_class import Stack
s = Stack()

postfix = input("Enter postfix expression ")

prefix = ''
for i in postfix:
    if i.isalpha():
        s.push(i)
    else:
        op1 = s.peek()
        s.pop()
        op2 = s.peek()
        s.pop()
        prefix = i + op2 + op1
        s.push(prefix)
    
print(prefix)