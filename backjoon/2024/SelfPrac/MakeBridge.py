# 다리만들기 (2146)
## 난이도 : 골드 3

import sys
import heapq
input = sys.stdin.readline

area_cnt = int(input())
zone = []
move_r = [-1,0,+1,0]
move_c = [0,-1,0,+1]
INT_MAX = sys.maxsize

for _ in range(area_cnt):
    zone.append(list(map(int, input().split())))


def check_zone(now_r, now_c, zone_num):
    global zone, visited
    visited[now_r][now_c] = True
    zone[now_r][now_c] = zone_num
    for i in range(4):
        next_r, next_c = now_r + move_r[i], now_c + move_c[i]
        if 0 <= next_r < area_cnt and 0 <= next_c < area_cnt:
            if not visited[next_r][next_c] and zone[next_r][next_c] != 0:
                visited[next_r][next_c] = True
                zone[next_r][next_c] = zone_num
                check_zone(next_r, next_c, zone_num)


now_zone = 1
visited = [[False for _ in range(area_cnt)] for _ in range(area_cnt)]
for r_idx in range(area_cnt):
    for c_idx in range(area_cnt):
        if not visited[r_idx][c_idx] and zone[r_idx][c_idx] != 0:
            check_zone(r_idx, c_idx, now_zone)
            now_zone += 1


def find_bridge(now_r, now_c, now_val):
    global find_move_visitied, INT_MAX
    find_move_visitied[now_r][now_c] = True
    hq = []
    heapq.heappush(hq, (0, now_r, now_c))
    #queue = deque([(now_r, now_c, 0)])
    while hq:
        val ,r, c = heapq.heappop(hq)
        for m in range(4):
            next_r, next_c = r + move_r[m], c + move_c[m]
            if 0 <= next_r < area_cnt and 0 <= next_c < area_cnt and not find_move_visitied[next_r][next_c]:
                if zone[next_r][next_c] == 0:
                    find_move_visitied[next_r][next_c] = True
                    heapq.heappush(hq, (val+1, next_r, next_c))
                elif zone[next_r][next_c] != now_val:
                    INT_MAX = min(val, INT_MAX)
                    return

find_move_visitied = [[False for _ in range(area_cnt)] for _ in range(area_cnt)]
for r_idx in range(area_cnt):
    for c_idx in range(area_cnt):
        if not find_move_visitied[r_idx][c_idx] and zone[r_idx][c_idx] != 0:
            find_bridge(r_idx, c_idx, zone[r_idx][c_idx])
            find_move_visitied = [[False for _ in range(area_cnt)] for _ in range(area_cnt)]

print(INT_MAX)