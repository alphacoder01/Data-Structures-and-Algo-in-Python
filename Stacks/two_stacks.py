'''
This code provides an efficient implementaion of 2 stacks in same array
'''

n = int(input("Enetr the size of the array"))
array = [0]*n

top_s1 = 0
top_s2 = len(array) - 1 
diff = top_s2 - top_s1

def push(s , n):
    if s == 's1':
        array[top_s1] = n
        top_s1 += 1
    elif s == 's2':
        array[top_s2] = n
        top_s2 -= 1

def pop(s):
    if s == 's1':
        array[top_s1] = 0
        top_s1 -= 1
    elif s == 's2':
        array[top_s2] = 0
        top_s2 += 1


while(1):
    print("[1] for pushing onto stack 1.")
    print("[2] for popping from stack 1.")
    print("[3] for pushing onto stack 2.")
    print("[4] for popping from stack 2.")
    print("[5] print stack 1.")
    print("[6] print stack 2.")
    print("[7] to exit.")

    user_io = int(input())

    if(user_io == 1 and diff != 0):
        x = int(input("Enter number"))
        push('s1',x)
        diff -= 1
    elif(user_io == 2 and diff != 0):
        pop('s1')
        diff += 1
    elif(user_io == 3 and diff != 0):
        x = int(input("Enter number"))
        push('s2' ,x)
        diff -= 1
    elif(user_io == 4 and diff != 0):
        pop('s2')
        diff += 1
    elif(user_io == 5):
        print(array[0:top_s1])
    elif(user_io == 6):
        print(array[top_s2:-1])
    elif(user_io == 7):
        print("Thank You!")
        SystemExit(0)


    

