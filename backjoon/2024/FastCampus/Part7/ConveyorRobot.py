# 컨베이어 위의 로봇 
## 골드 5

import sys
from collections import deque
input = sys.stdin.readline 

size_conveyor, size_end = list(map(int, input().split()))
temp = list(map(int, input().split()))
conveyor = deque([])
for num in temp:
    conveyor.append([num,-1])

answer = 0

while True:
    answer += 1 # 현재 단계를 카운트하는 변수

    #1.벨트가 각 칸 위에 로봇과 함께 한 칸 회전
    conveyor.rotate(1)
    conveyor[size_conveyor-1][1] = -1
    
    #2. 로봇을 벨트가 회전하는 방향으로 이동
    for idx in range(size_conveyor-1, 0, -1):
        if conveyor[idx][1] != -1:
            continue
        if conveyor[idx-1][1] != -1 and conveyor[idx][0] != 0:
            
            conveyor[idx][1] = conveyor[idx-1][1]
            conveyor[idx-1][1] = -1
            conveyor[idx][0] -= 1
            if conveyor[idx][0] == 0:
                size_end -= 1

    conveyor[size_conveyor-1][1] = -1

    #3.내구도가 0이 아닌 벨트에 로봇을 올림
    if conveyor[0][0] != 0:
        conveyor[0][1] = 1
        conveyor[0][0] -= 1
        if conveyor[0][0] == 0:
            size_end -= 1

    #4.내구도가 0인 칸이 조건에 맞으면 종료
    if size_end <= 0:
        print(answer)
        break