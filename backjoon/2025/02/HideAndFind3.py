# 숨바꼭질 3
## 난이도 : 골드 5

import sys
from collections import deque
input = sys.stdin.readline

me, sibling = list(map(int, input().split()))
visited = [sys.maxsize for _ in range(100001)]
answer = sys.maxsize

def backTracking(now, time):
    global answer
    next_go = deque([(now, time)])

    while next_go:
        now_go, now_time = next_go.popleft()
        if now_go == sibling:
            answer = min(answer, now_time)
        
        if now_go * 2 < 100001 and visited[now_go * 2] > now_time:
            visited[now_go * 2] = now_time
            next_go.append((now_go * 2, now_time))
        if now_go + 1 < 100001 and visited[now_go + 1] > now_time:
            next_go.append((now_go + 1, now_time + 1))
            visited[now_go + 1] = now_time
        if now_go - 1 >= 0 and visited[now_go - 1] > now_time:
            next_go.append((now_go - 1, now_time + 1))
            visited[now_go - 1] = now_time

backTracking(me, 0)
print(answer)