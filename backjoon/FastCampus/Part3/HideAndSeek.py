# 숨박꼭질 (1697)

import sys
from collections import deque

MAX_INT = sys.maxsize
input = sys.stdin.readline

start, end = list(map(int, input().split()))
visited = set()
visited.add(start)
save = deque([(start,0)])
result = 0

def bfs():
    global visited
    global result
    global start
    global end
    global save
    
    while save:
        node, cnt = save.popleft()
        cnt += 1
        
        if (node-1 > -1 and node-1 not in visited):
            if (node-1 == end):
                result = cnt
                break
            visited.add(node-1)
            save.append((node-1, cnt))
        if (node+1 <= 100000 and node+1 not in visited):
            if (node+1 == end):
                result = cnt
                break
            visited.add(node+1)
            save.append((node+1, cnt))
        if (node*2 <= 100000 and node*2 not in visited):
            if (node*2 == end):
                result = cnt
                break
            visited.add(node*2)
            save.append((node*2,cnt))

bfs()
print(result)
