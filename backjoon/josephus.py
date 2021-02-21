import sys
input = sys.stdin.readline

num = input()
num = int(num)
param = input()
param = int(param)
queue = [i + 1 for i in range(num)]
out = 0
size = len(queue) - 1 

for i in range(num):
    out = out + param - 1
    if out > size:
        out = out - size - 1

    size += -1
    print(queue.pop(out))