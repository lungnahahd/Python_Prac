a,b = input().split()
print(a)
print(b)


num = input()
num = int(num)
stack = []
count = 0
top = 0
while count != num:
    call = input()

    if call == "top":
        if not stack:
            print("-1")
        else:
            print(stack[0])
    elif call == "pop":
        if not stack:
            print("-1")
        else:
            print(stack[0])
            temp = []
            for i in range(len(stack) + 1):
                temp[i] = stack[i+1]
            stack = temp
    elif call == "size":
        print(len(stack))
    elif call == "empty":
        if stack is not None:
            print("0")
        else:
            print("1")
    else :
        call,param = input().split()
        param = int(param)
        stack[top] = param
        top += 1
    count += 1