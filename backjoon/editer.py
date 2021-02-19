import sys
input = sys.stdin.readline

import sys
input = sys.stdin.readline

stack1 = input().strip()
stack1 = list(stack1)
num = input()
num = int(num)

stack2 = []
cursor = len(stack1) - 1
size = len(stack1) - 1

for i in range(num):
    call = input().strip()
    if call == "L":
        if cursor == -1:
            continue
        else:
            cursor += -1
    elif call == "D":
        if cursor == size:
            continue
        else:
            cursor += 1
    elif call == "B":
        if cursor == -1:
            continue
        else:
            stack1.pop(cursor)
            cursor += -1
    else:
        call, param = call.split()
        stack1.insert(cursor + 1 , param)
        cursor += 1

print(''.join(stack1))












# 시간 초과 발생

# first_str = input().strip()
# first_arr = list(first_str)
# num = input()
# num = int(num)
# cursor = len(first_arr)

# for i in range(num):
#     call = input().strip()
#     if call == "L":
#         if cursor == 0:
#             continue
#         else:
#             cursor += -1
#     elif call == "D":
#         if cursor == len(first_str):
#             continue
#         else:
#             cursor += 1
#     elif call == "B":
#         if cursor == 0:
#             continue
#         else:
#             # print(cursor)
#             del first_arr[cursor -1 ]
#             cursor += -1
#     else:
#         call, param = call.split()
#         first_arr.insert(cursor , param)
#         cursor += 1
        
# print(''.join(first_arr))