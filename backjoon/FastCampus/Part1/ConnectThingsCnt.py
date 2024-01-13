# 연결 요소의 개수 (11724)
## 난이도 : 중

import sys
from collections import deque
input = sys.stdin.readline

node_cnt, line_cnt = list(map(int, input().split()))
mothers = [idx for idx in range(node_cnt+1)] # 부모 리스트
link_state = [[] for _ in range(node_cnt+1)] # 연결 상태를 나타내는 리스트
visited = [False for _ in range(node_cnt+1)] # 방문 여부 리스트
will_go = deque([])

# 연결 리스트 상태를 갱신하는 과정 (양방향 그래프 기준)
for _ in range(line_cnt):
    x, y = list(map(int, input().split()))
    link_state[x].append(y)
    link_state[y].append(x)

# 양방향 그래프 기준 부모 리스트 갱신
for now in range(1, node_cnt):
    if visited[now]:
        continue
    will_go.append(now)
    
    while will_go: # 루트 노드(작은 수)를 기준으로 연결된 것들부터 우선 방문
        now = will_go.popleft()
        if visited[now]:
            continue
        visited[now] = True
        for go_node in link_state[now]:
            if visited[go_node]:
                continue
            will_go.append(go_node)
            mothers[go_node] = mothers[now]

set_mother = set()

for idx in range(1,node_cnt+1):
    now_num = mothers[idx]
    if now_num in set_mother:
        continue
    set_mother.add(now_num)

print(len(set_mother))