
a, b, v = input().split()
up = int(a)
down = int(b)
length = int(v)


if __main__ == "__main__":
    num = input()
    num = int(num)
    stack = []
    count = 0
    top = 0
    while count != num:
        call = input()
        call, param = input().split()
        param = int(param)

        if call == "push":
            stack[top] = param
            top += 1
        elif call == "pop":
            if call is not None:
                print(call[0])
                temp = []
                for i in range(len(call) + 1):
                    temp[i] = call[i+1]
                call = temp
            else:
                print("-1")
        elif call == "size":
            print(len(call))
        elif call == "empty":
            if call is not None:
                print("0")
            else:
                print("1")
        else :
            if call is not None:
                print(call[0])
            else:
                print("-1")


        count += 1