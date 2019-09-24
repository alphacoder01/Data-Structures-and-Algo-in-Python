from collections import deque
import sys
mystack = deque()

def show(s):
    print(mystack)

while(1):
    print("[1] for pushing onto stack.")
    print("[2] for popping from stack.")
    print("[3] to exit.")
    user_io = int(input('Enter your choice:'))
    
    if(user_io == 1):
        x = int(input('Enter number'))
        mystack.append(x)
        show(mystack)
    elif(user_io == 2):
        mystack.pop()
        show(mystack)
    else:
        print("Thank You!")
        sys.exit(0)


    