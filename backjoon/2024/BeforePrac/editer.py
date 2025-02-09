import sys
input = sys.stdin.readline

getstr = input().strip()
getstr = list(getstr)
stack = []

num = input()
num = int(num)

for i in range(num):
    call = input().strip()
    if call[0] == "L":
        if len(getstr) == 0:
            continue
        stack.append(getstr.pop())
    elif call[0] == "B":
        if len(getstr) == 0:
            continue
        getstr.pop()
    elif call[0] == "D":
        if len(stack) == 0:
            continue
        getstr.append(stack.pop())
    else:
        getstr.append(call[2]) 
final = "".join(getstr)
final2 = stack[::-1]
final2 = "".join(final2)


print(final + final2)