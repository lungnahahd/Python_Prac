# 8 * 8의 좌표 평면상에서 나이트의 위치가 주어졌을 경우, 나이트가 이동할 수 있는 경우의 수를 출력
# 좌표의 행의 위치는 1부터 8까지 표현, 열의 위치는 a부터 h까지 표현
# 현재 나이트가 위치한 좌표가 제공되면 나이트가 이동할 수 있는 경우의 수를 출력

import sys
input = sys.stdin.readline

knight = input()
row = int(knight[1]) - 1
col = ord(knight[0]) - 97 # 아스키코드로 문자를 숫자로 변형
dx = [0,0,-2,2]
dy = [-2,2,0,0]
count = 0

for i in range(4):
    if 0 <= row + dx[i] <= 7 and 0 <= col + dy[i] <= 7:
        change_row = row + dx[i]
        change_col = col + dy[i]
        if i < 2:
            if row + 1 <= 7:
                count += 1
            if row -1 >= 0:
                count += 1
        else:
            if col + 1 <= 7:
                count += 1
            if col -1 >= 0:
                count += 1
                
print(count)

# 참고 답안
# 여기서는 방향 벡터를 x와 y로 나누지 않고 한 번에 접근
# 여기서 갈 수 있는 8가지 방향을 모두 방향 벡터를 활용해서 처리

# input_data = input()
# row = int(input_data[1])
# col = int(ord(input_data[0])) - int(ord('a')) + 1
# # 8가지 방향을 모두 방향 벡터로 표시
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_col = col + step[1]

#     if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
#         result +=1 
# print(result)