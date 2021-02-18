import sys
input = sys.stdin.readline

first_str = input().strip()
num = input()
num = int(num)
cursor = len(first_str)

for i in range(num):
    call = input().strip()
    if call == "L":
        if cursor == 0:
            continue
        else:
            cursor += -1
    elif call == "D":
        if cursor == len(first_str):
            continue
        else:
            cursor += 1
    elif call == "B":
        if cursor == 0:
            continue
        else:
            if cursor == len(first_str):
                first_str = first_str[:len(first_str)-1]
                cursor += -1
            else:
                first_str = first_str[: cursor-1] + first_str[cursor:]
                cursor += -1
    else:
        call, param = call.split()
        if cursor == 0:
            first_str = param + first_str
            cursor += 1
        elif cursor == len(first_str):
            first_str = first_str + param
            cursor += 1
        else:
            first_str = first_str[:cursor] + param + first_str[cursor:]
            cursor += 1

print(first_str)