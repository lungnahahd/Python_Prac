import sys
input = sys.stdin.readline

num = input()
num = int(num)
stack = [0 for i in range(num)]
head = 0
check = 1
re_check = 0
result = [0 for i in range(num * 2)]
flag = True

for i in range(num):
    getnum = input()
    getnum = int(getnum)
    if flag:
        while check <= getnum:
            stack[head] = check
            head += 1
            check += 1
            result[re_check] = "+"
            re_check += 1
        if stack[head - 1] == getnum:
            stack[head - 1] = 0
            head += -1
            result[re_check] = "-"
            re_check += 1
        else:
            flag = False

if flag :
    for i in range(re_check):
        print(result[i])
else:
    print("NO")
