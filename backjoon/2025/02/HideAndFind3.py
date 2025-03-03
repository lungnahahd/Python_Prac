# 숨바꼭질 3
## 난이도 : 골드 5

import sys
from collections import deque
input = sys.stdin.readline

me, sibling = list(map(int, input().split()))
not_visited = [True for _ in range(100001)]

def backTracking(now, time):

    next_go = deque([(now, time)])

    while next_go:
        now_go, now_time = next_go.popleft()
        if now_go == sibling:
            print(now_time)
            return
        next_go.append((now_go * 2, now_time))
        next_go.append((now_go + 1, now_time + 1))
        next_go.append((now_go - 1, now_time + 1))

backTracking(me, 0)