import sys
input = sys.stdin.readline

size = input().strip()
size = int(size)
count = size - 1
num = [0 for i in range(size)]
check = 0
final = ""
stack = []
result = [0 for i in range(size)]

num = list(map(int, input().strip().split()))

for i in range(size):
    while j in range(count):
        check = num.pop()
        if check > num[i]:
            stack.append(check)
        num.insert(0, check)
        num.pop()
        
print()
        



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