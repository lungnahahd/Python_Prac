# 환승 (5214)
## 난이도 : 골드 2

import sys
input = sys.stdin.readline
INT_MAX = sys.maxsize
# 9 3 5
# 1 2 3
# 1 4 5
# 3 6 7
# 5 6 7
# 6 8 9

node_cnt, connect_cnt, hypertube_cnt = list(map(int, input().split()))
nodes = [[] for _ in range(node_cnt+1)] # 하이퍼 튜브를 가지는 노드
for _ in range(hypertube_cnt):
    temp = list(map(int, input().split()))
    for main in temp:
        for insert in temp:
            if insert == main:
                continue
            nodes[main].append(insert)

visited = [False for _ in range(node_cnt + 1)]
result = INT_MAX
def bfs_hyper(start, visit, cost):
    global result

    if start == node_cnt:
        result = min(result, cost)

    for hyper in nodes[start]:

        if visit[hyper]:
            continue
        visit[hyper] = True
        bfs_hyper(hyper, visit, cost+1)
        visit[hyper] = False
bfs_hyper(1, visited, 1)
if result == INT_MAX:
    print(-1)
else:
    print(result)