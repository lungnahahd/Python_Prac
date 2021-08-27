import sys
input = sys.stdin.readline

beforeOne = int(input())

count = 0
while beforeOne != 1:
    if beforeOne %  3 == 0:
        beforeOne = beforeOne / 3 
        count += 1
    elif (beforeOne - 1) % 3 == 0:
        beforeOne = (beforeOne -1) / 3
        count += 2 
    elif beforeOne % 2 == 0:
        beforeOne = beforeOne / 2
        count += 1
    else:
        beforeOne -= 1
        count += 1
print(count)