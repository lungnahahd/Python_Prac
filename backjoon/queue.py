import sys
input = sys.stdin.readline

num = input()
num = int(num)
queue = [0 for i in range(num)]
head = 0
tail = 0
count = 0

while count != num:
    call = input().strip()
    if call == "front" :
        if head == tail:
            print("-1")
        else:
            print(queue[head])
    elif call == "back":
        if head == tail:
            print("-1")
        else:
            print(queue[tail - 1])
    elif call == "empty":
        if head == tail:
            print("1")
        else:
            print("0")
    elif call == "size":
        print(tail - head)
    elif call == "pop":
        if head == tail:
            print("-1")
        else:
            print(queue.pop(head))
            tail += -1
    else:
        call, param = call.split()
        param = int(param)
        queue[tail] = param
        tail += 1
    count += 1