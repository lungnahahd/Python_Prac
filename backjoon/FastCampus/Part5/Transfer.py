# 환승 (5214)
## 난이도 : 골드 2

import sys
from collections import deque
input = sys.stdin.readline

INT_MAX = sys.maxsize
# 9 3 5
# 1 2 3
# 1 4 5
# 3 6 7
# 5 6 7
# 6 8 9

node_cnt, connect_cnt, hypertube_cnt = list(map(int, input().split()))
nodes = [[] for _ in range(node_cnt+hypertube_cnt+1)] # 하이퍼 튜브와 노드를 함께 가지는 리스트 
for hyper_idx in range(hypertube_cnt):
    temp = list(map(int, input().split()))
    for node_idx in temp:
        nodes[node_idx].append(hyper_idx+1+node_cnt) # 각 노드에 하이퍼 튜브 값을 추가
        nodes[node_cnt+hyper_idx+1].append(node_idx) # 하이퍼 튜브에 대한 정보를 추가 

visited = [False for _ in range(node_cnt + hypertube_cnt + 1)]
result = INT_MAX

def v2_hyper(start):
    global result, visited
    dq = deque([(start, 1)])
    if start == node_cnt:
        result = 1
        return

    while dq:
        go, cost = dq.popleft()
        for next_go in nodes[go]:
            if next_go == node_cnt:
                result = (cost // 2+1)
                return
            if visited[next_go]:
                continue
            dq.append((next_go, cost+1))
            visited[next_go] = True
visited[1] = True
v2_hyper(1)
if result == INT_MAX:
    print(-1)
else:
    print(result)