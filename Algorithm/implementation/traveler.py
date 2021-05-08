# 크기를 나타내는 N이 주어지고, 여행가의 이동 계획 내용이 제공
# 여행가가 최종적으로 도착할 지점의 좌표를 공백을 기준으로 구분하여 출력

import sys
input = sys.stdin.readline

move = input().strip()
move = int(move)

space_array = [[0] * move for _ in range(move)]
start_l = 1
start_r = 1

moveplan = input().strip()
# moveplan 공백 지우기
moveplan = moveplan.replace(" ","")

for i in range(len(moveplan)):
    if moveplan[i] == "R":
        if (start_r + 1) == (move + 1):
            continue
        start_r = start_r + 1
    elif moveplan[i] == "L":
        if (start_r - 1) == 0:
            continue
        start_r = start_r - 1
    elif moveplan[i] == "U":
        if (start_l - 1) == 0:
            continue
        start_l = start_l - 1
    elif moveplan[i] == "D":
        if (start_l + 1) == (move + 1):
            continue
        start_l = start_l + 1

print(str(start_l) + " " + str(start_r))