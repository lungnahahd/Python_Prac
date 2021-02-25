import sys
input = sys.stdin.readline

size = input().strip()
size = int(size)
count = 0
num = [0 for i in range(size)]
getnum = input().strip()
length = len(getnum)
check = 0
final = ""
result = [0 for i in range(size)]

for i in range(size - 1):
    num[i], getnum = getnum.split(' ',maxsplit=1)
num[size -1 ] = getnum

for i in range(size-1):
    result[i] = num[i]
    for j in range(size - i):
        if num[i] < num[j + i]:
            result[i] = num[j+ i]
            final = final + str(result[i]) + ' '
            break
    if result[i] == num[i]:
        result[i] = -1
        final = final + str(result[i]) + ' '

final = final + "-1"

print(final)
