# 연구소3
########################
# 처음 모든 바이러스는 비활성, 활성 상태는 상하좌우로 인접한 빈 칸에 동시 복제 -> 1초 필요
# 목표 -> 바이러스 M개를 활성상태로 변경
# 활성이 비활성이 있는 칸으로 가면 비활성이 활성으로 변경
# 0은 빈 칸, 1은 벽, 2는 바이러스 위치
# N은 연구소의 크기, M은 처음에 활성화 시킬 수 있는 바이러스 개수
# 모든 빈 카에 바이러스가 있게 되는 최소 시간을 출력, 모든 칸에 퍼트릴 수 없는 경우는 -1 출력

import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
station = []
zero_room = 0
not_active_virus = []
for cnt in range(n):
    temp = list(map(int, input().split()))
    zero_room += temp.count(0)
    for idx, info in enumerate(temp):
        if info == 2:
            not_active_virus.append((cnt, idx))
    station.append(temp)

moves = [[+1, 0], [0, +1], [-1, 0], [0, -1]]


def bfs(starts, station):
    save = deque()
    make_virus = 0
    for row, col in starts:
        save.append((row, col, 0))
        station[row][col] = 1
    result_time = 0
    while save and make_virus != zero_room:
        now_row, now_col, time = save.popleft()
        for move in moves:
            next_row, next_col = now_row + move[0], now_col + move[1]
            if 0 <= next_row < n and 0 <= next_col < n and station[next_row][next_col] != 1:
                if station[next_row][next_col] == 0:
                    make_virus += 1
                save.append((next_row, next_col, time+1))
                result_time = max(result_time, time+1)
                station[next_row][next_col] = 1
    if make_virus != zero_room:
        result_time = sys.maxsize
    return result_time


can_select_active = list(combinations(not_active_virus, m))
answer = sys.maxsize
for select_active in can_select_active:
    case_station = copy.deepcopy(station)
    now_case_time = bfs(select_active, case_station)
    answer = min(answer, now_case_time)
if answer == sys.maxsize:
    answer = -1
print(answer)
