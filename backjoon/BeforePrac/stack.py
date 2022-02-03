import sys
input = sys.stdin.readline



num = input()
num = int(num)
stack = [0 for i in range(num)]
count = 0
top = -1

head = -1

while count != num:
    call = input().strip()
    if call == "top" :
        if head == -1 :
            print("-1")
        else:
            print(stack[head])
    elif call == "pop":
        if head == -1:
            print("-1")
        else : 
            print(stack[head])
            stack[head] = 0
            head += -1
    elif call == "size":
        print(head + 1)
    elif call == "empty":
        if head == -1:
            print("1")
        else:
            print("0")
    elif call[0:4] == "push":
        call, param = call.split()
        param = int(param)
        head += 1
        stack[head] = param
    count += 1