# 톱니바퀴 (14891)
## 난이도 : 골드 5

import sys
from collections import deque
input = sys.stdin.readline

gears = []

for _ in range(4):
    gear = list(input())
    gears.append(deque(gear[:-1]))
    
def turn_time_way(gear_dq):
    temp = gear_dq.pop()
    gear_dq.appendleft(temp)
    return gear_dq

def turn_reverse_time_way(gear_dq):
    temp = gear_dq.popleft()
    gear_dq.append(temp)
    return gear_dq

cnt = int(input())
for _ in range(cnt):
    num, turn_way = list(map(int, input().split()))
    num -= 1
    left, right = -1, -1
    left_gear, right_gear = num - 1, num + 1
    left, right = gears[num][6], gears[num][2]
    if left_gear >= 0 and gears[left_gear][2] != left:
        if turn_way == -1:
            left_gear_turn = 1
        else:
            left_gear_turn = -1

        while left_gear >= 0:
            before_left = gears[left_gear][6]
            if left_gear_turn == 1:
                turn_time_way(gears[left_gear])
            else:
                turn_reverse_time_way(gears[left_gear])
            if left_gear - 1 >= 0:
                if gears[left_gear-1][2] != before_left:
                    left_gear -= 1
                    left_gear_turn = left_gear_turn * -1
                else:
                    break
            else:
                break
    if right_gear < 4 and right != gears[right_gear][6]:
        if turn_way == -1:
            right_gear_turn = 1
        else:
            right_gear_turn = -1

        while right_gear < 4:
            before_right = gears[right_gear][2]
            if right_gear_turn == 1:
                turn_time_way(gears[right_gear])
            else:
                turn_reverse_time_way(gears[right_gear])
            if right_gear + 1 < 4:
                if gears[right_gear+1][6] != before_right:
                    right_gear += 1
                    right_gear_turn = right_gear_turn * -1
                else:
                    break
            else:
                break

    if turn_way == 1:
        turn_time_way(gears[num])
    else:
        turn_reverse_time_way(gears[num])

result = 0
value = 0
for gear in gears:
    cost = 2**value
    if gear[0] == '1':
        result += cost
    value += 1
print(result)