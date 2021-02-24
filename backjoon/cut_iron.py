import sys
input = sys.stdin.readline

iron = input().strip()
iron = list(iron)
count = len(iron)
setnum = 0
result = 0
check = False

for i in range(count):
    if check:
        check = False
    else:
        if iron[i] == "(":
            if iron[i+1] == ")":
                check = True
                result += setnum
            else:
                setnum += 1
        else:
            setnum += -1
            result += 1
print(result)