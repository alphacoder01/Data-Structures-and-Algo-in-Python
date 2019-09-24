'''
This code provides an efficient implementaion of 2 stacks in same array
'''
import sys
n = int(input("Enter the size of the array"))
array = [0]*n

def push(s , n,top_s1,top_s2):
    if s == 's1':
        array[top_s1] = n
        return top_s1+1
    elif s == 's2':
        array[top_s2] = n
        return top_s2 -1 

def pop(s,top_s1,top_s2):
    if s == 's1':
        array[top_s1-1] = 0
        return top_s1 - 1
    elif s == 's2':
        array[top_s2 +1 ] = 0
        return top_s2 +1 

if __name__ == "__main__":
    top_s1 = 0
    top_s2 = len(array) - 1 
    diff = top_s2 - top_s1

    while(1):
        print("[1] for pushing onto stack 1.")
        print("[2] for popping from stack 1.")
        print("[3] for pushing onto stack 2.")
        print("[4] for popping from stack 2.")
        print("[5] print stack 1.")
        print("[6] print stack 2.")
        print("[7] to exit.")

        user_io = int(input())

        if(user_io == 1 ):
            if(diff < 0 ):
                print("Stack full!")
                pass
            x = int(input("Enter number"))
            top_s1 =  push('s1',x,top_s1,top_s2)
            diff -= 1
            
                
        elif(user_io == 2 ):
            top_s1 = pop('s1',top_s1,top_s2)
            diff += 1

        elif(user_io == 3):
            if(diff < 0):
                print("Stack full!")
                pass
            x = int(input("Enter number"))
            top_s2 = push('s2' ,x,top_s1,top_s2)
            diff -= 1
        
        elif(user_io == 4 ):
            top_s2 = pop('s2',top_s1,top_s2)
            diff += 1

        elif(user_io == 5):
            print(array[0:top_s1])
            # print(array)

        elif(user_io == 6):
            print(array[top_s2:-1])
            # print(array)

        elif(user_io == 7):
            print("Thank You!")
            sys.exit(0)


    

