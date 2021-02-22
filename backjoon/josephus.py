import sys
input = sys.stdin.readline


num, param = input().split()
num = int(num)
param = int(param)
queue = [i + 1 for i in range(num)]
final = [0 for i in range(num)]
out = 0
size = len(queue) 

for i in range(num):
    out = out + param - 1
    while out > size - 1:
        out = out - size
      
    size += -1
    final[i] = queue.pop(out)
if num == 1:
    print("<1>")
else:
    for i in range(num):
        if i == 0:
            print("<" + str(final[i]) + ", ",end="")
        elif i == num -1:
            print(str(final[i]) + ">",end="")
        else:
            print(str(final[i]) + ", ",end="")