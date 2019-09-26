from stack_class import Stack
s = Stack()

postfix = input("Enter postfix expression ")

infix = ''
for i in postfix:
    if i.isalpha():
        s.push(i)
    else:
        op1 = s.peek()
        s.pop()
        op2 = s.peek()
        s.pop()
        infix = op2 + i + op1
        infix = '(' + infix + ')'
        s.push(infix)
    
print(infix)