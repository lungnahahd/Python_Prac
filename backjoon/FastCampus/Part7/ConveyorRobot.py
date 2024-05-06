# 컨베이어 위의 로봇 
## 골드 5

import sys
import heapq
from collections import deque
input = sys.stdin.readline 

size_conveyor, size_end = list(map(int, input().split()))
conveyor = list(map(int, input().split()))
conveyor = deque(conveyor)
answer = 0
robot = deque([-1 for _ in range(size_conveyor * 2)])

while True:
    #1.벨트가 각 칸 위에 로봇과 함께 한 칸 회전
    temp = conveyor.pop()
    conveyor.appendleft(temp)
    for idx in range(size_conveyor*2):
        if robot[idx] == -1:
            continue
        else:
            move = idx + 1
            if move == size_conveyor*2:
                move = 0
            elif move == size_conveyor-1:
                move = -1
            robot[idx] = move


    #2.로봇을 벨트가 회전하는 방향으로 이동
    for idx in range(size_conveyor * 2):
        if robot[idx] == -1:
            continue

        next_idx = robot[idx] + 1
        if next_idx == size_conveyor * 2:
            next_idx = 0
            if conveyor[next_idx] == 0:
                next_idx = idx
            else:
                conveyor[next_idx] -= 1
                if conveyor[next_idx] == 0:
                    size_end -= 1
        elif next_idx == size_conveyor - 1:
            next_idx = -1
        robot[idx] = next_idx
    
    #3.내구도가 0이 아닌 벨트에 로봇을 올림
    if conveyor[0] != 0:
        robot.append(0)
        conveyor[0] -= 1
        if conveyor[0] == 0:
            size_end -= 1
    
    if size_end == 0:
        print(answer)
        break
    
    answer += 1
