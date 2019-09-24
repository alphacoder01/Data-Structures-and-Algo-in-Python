'''
This special stack is similar to the normal stack having operations like push(), pop(), peek()
but with one extra operation i.e getMin() which gives the minimum element in stack, and all the operations
must be perfromed in O(1) time
'''


'''
The approach is to use a auxillary stack to store the minimum value at the top along with a normal stack.
'''
from stack_class import Stack
import sys

original_stack = Stack()
auxillary_stack = Stack()

while(1):
    print("[1] for pushing onto stack.")
    print("[2] for popping from stack.")
    print("[3] to get minimum from stack.")
    print("[4] to exit")

    user_io = int(input('Enter your choice:'))
    
    if(user_io == 1):
        x = int(input('Enter number'))
        original_stack.push(x)
    
        if(auxillary_stack.is_empty()):
            auxillary_stack.push(x)

        elif(x < auxillary_stack.peek()):
            auxillary_stack.push(x)

    elif(user_io == 2):
        if(original_stack.peek() == auxillary_stack.peek()):
            original_stack.pop()
            auxillary_stack.pop()
        else:
            original_stack.pop()
    elif(user_io == 3):
        print(auxillary_stack.peek())
    
    else:
        print("Thank You")
        sys.exit(0)

