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


# # 참고 답안
# n = int(input()) # 입력 받기
# x, y = 1, 1 # 초기 위치 설정
# plans = input().split() # 입력 받기
# # 방향 벡터를 활용하기(위아래를 한 쌍으로 보기)
# dx = [0,0,-1,1]
# dy = [-1,1,0,1]
# move_types = ['L', 'R', 'U', 'D']
# #이동 계획을 하나씩 확인하기
# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     # 공간을 벗어나는 경우 무시
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     # 이동 수행
#     x, y = nx, ny
# print(x,y)