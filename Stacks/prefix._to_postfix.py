from stack_class import Stack           #importing the stack class
s = Stack()                             #Stack object

postfix = ''                                      
prefix = input("Enter the prefix string ")
prefix_reversed = reversed(prefix)      #reversed prefix srting

for i in prefix_reversed:
    if i.isalpha():                     #if i is operand then push onto stack
        s.push(i)
    else:
        op1 = s.peek()                 #else pop 2 operands from stack and form a string as shown 
        s.pop()
        op2 = s.peek()
        s.pop()
        postfix = op1 + op2 + i
        # for infix --> op1 + i + op2
        s.push(postfix)                   #finally push the string onto the stack.
print(postfix)

