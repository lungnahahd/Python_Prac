# 우주신과의 교감 (1774)
## 난이도 : 중

import sys
import math
import heapq

input = sys.stdin.readline


# 두 점 사이 거리 구하기
def chkDist(a,b):
    x_long = a[0] - b[0]
    y_long = a[1] - b[1]
    return math.sqrt((x_long * x_long) + (y_long * y_long))

god_cnt, connect_cnt = list(map(int, input().split()))

god_place_list = []

before_connect = set()

for _ in range(god_cnt):
    x, y = list(map(int,input().split()))
    god_place_list.append((x,y))

for _ in range(connect_cnt):
    temp_a, temp_b = list(map(int, input().split()))
    a, b = temp_a - 1, temp_b - 1
    before_connect.add((min(a,b), max(a,b)))

dist_heap = []

for start in range(len(god_place_list)-1):
    for end in range(start+1, len(god_place_list)):
        if ((start,end) in before_connect):
            continue
        now_dist = chkDist(god_place_list[start], god_place_list[end])
        heapq.heappush(dist_heap, now_dist)

need_connect = god_cnt - 1 - connect_cnt

answer = 0

for _ in range(need_connect):
    answer += heapq.heappop(dist_heap)

print(round(answer,1))