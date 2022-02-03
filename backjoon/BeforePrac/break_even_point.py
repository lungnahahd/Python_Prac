import math
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if b>c or b==c:
    print(-1)
else:
    num = a / (c-b)
    num = math.floor(num) + 1
    print(num)
