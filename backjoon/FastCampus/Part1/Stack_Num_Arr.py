# 스택 수열 (1874)

size = int(input())
num_stack = []
now_num = 1
result = []
say_no = False
num_stack.append(0)

for _ in range(size):
    target = int(input())
    if (say_no):
        continue
    while num_stack:
        if (now_num < target):
            num_stack.append(now_num)
            now_num += 1
            result.append("+")
        elif (now_num > target):
            if (target == num_stack[-1]):
                result.append("-")
                num_stack.pop()
                break
            else:
                say_no = True
                break
        elif (now_num == target):
            now_num += 1
            result.append("+")
            result.append("-")
            break

if (not say_no):
    for say in result:
        print(say)
else:
    print("NO")