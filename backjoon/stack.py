
num = input()
num = int(num)
stack = [0 for i in range(num)]
count = 0
top = -1
while count != num:
    call = input()

    if call == "top":
        if top == -1:
            print("-1")
        else:
            print(stack[top])
    elif call == "pop":
        if top == -1 :
            print("-1")
        else:
            print(stack[top])
            temp = [0 for i in range(num)]
            for i in range(top):
                temp[i] = stack[i]
            stack = temp
            top += -1
    elif call == "size":
        print(top + 1)
    elif call == "empty":
        if top == -1:
            print("1")
        else:
            print("0")
    elif call[0:4] == "push":
        call, param = call.split()
        param = int(param)
        top += 1
        stack[top] = param
    else :
        print("No Effect Order...")
    count += 1