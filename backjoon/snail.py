import math

a, b, v = input().split()
up = int(a)
down = int(b)
length = int(v)

go = up - down
length = length - up
day = math.ceil(length / go) + 1

print(day)