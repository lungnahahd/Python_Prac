# 숨박꼭질 (1697)

import sys

MAX_INT = sys.maxsize
input = sys.stdin.readline

start, end = list(map(int, input().split()))
visited = set()
visited.add(start)
result = MAX_INT

def bfs(node):
    global visited
    global result
    global start
    global end
    
    if (node-1 > -1 and node-1 not in visited):
        if (node-1 == end):
            result = min(result, node-1)
            return
        visited.add(node-1)
        bfs(node-1)
    if (node+1 <= 100000 and node+1 not in visited):
        if (node+1 == end):
            result = min(result, node+1)
            return
        visited.add(node+1)
        bfs(node+1)
    if (node*2 <= 100000 and node*2 not in visited):
        if (node*2 == end):
            result = min(result, node*2)
            return
        visited.add(node*2)
        bfs(node*2)

bfs(start)
print(result)
