# 바이러스 (2606)
## 난이도 : 하

import sys
from collections import deque

input = sys.stdin.readline 

cnt_computer = int(input()) # 컴퓨터(노드) 수
cnt_connect = int(input()) # 네트워크 연결 수 

network = [[] for _ in range(cnt_computer+1)]
visited = set()
# 네트워크를 입력 받고, 형성하는 과정
for _ in range(cnt_connect):
    a, b = list(map(int, input().split()))
    network[a].append(b)
    network[b].append(a)

# bfs 로 처리하는 과정 
dq_save = deque([1])
visited.add(1)
result = 0

while dq_save:
    now = dq_save.popleft()
    can_go = network[now]
    for go in can_go:
        if go not in visited:
            result += 1
            visited.add(go)
            dq_save.append(go)
print(result)