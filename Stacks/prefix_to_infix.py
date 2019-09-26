from stack_class import Stack
s = Stack()

infix = ''
prefix = input("Enter the prefix string ")
prefix_reversed = reversed(prefix)

for i in prefix_reversed:
    if i.isalpha():
        s.push(i)
    else:
        op1 = s.peek()
        s.pop()
        op2 = s.peek()
        s.pop()
        infix = op1 + i + op2
        infix = '('+infix+')'
        s.push(infix) 
print(infix)

