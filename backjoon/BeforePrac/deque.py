import sys
input = sys.stdin.readline

num = input()
num = int(num)
Deque = [0 for i in range(num)]
size = 0

for i in range(num):
    call = input().strip()
    if call == "size":
        print(size)
    elif call == "empty":
        if size == 0:
            print("1")
        else : 
            print("0")
    elif call == "front":
        if size == 0:
            print("-1")
        else:
            print(Deque[0])
    elif call == "back":
        if size == 0:
            print("-1")
        else:
            print(Deque[size-1])
    elif call == "pop_front":
        if size == 0:
            print("-1")
        else:
            print(Deque.pop(0))
            size += -1
    elif call == "pop_back":
        if size == 0:
            print("-1")
        else:
            print(Deque.pop(size-1))
            size += -1
    elif call[0:10] == "push_front":
        call, param = call.split()
        param = int(param)
        Deque.insert(0, param)
        size += 1
    else :
        call, param = call.split()
        param = int(param)
        Deque.insert(size, param)
        size += 1