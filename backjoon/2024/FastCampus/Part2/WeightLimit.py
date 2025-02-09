# 중량제한 (1939)
## 난이도 : 중상 

import sys
import copy

input = sys.stdin.readline

cnt_node, cnt_road = list(map(int, input().split()))

node_map = dict()


for _ in range(cnt_road): # 정보를 갱신하는 부분
    a_island, b_island, cost = list(map(int, input().split()))
    if a_island in node_map:
        node_map[a_island].append((b_island, cost))
    else:
        node_map[a_island] = [(b_island, cost)]
    if b_island in node_map:
        node_map[b_island].append((a_island, cost))
    else:
        node_map[b_island] = [(a_island, cost)]

start_point, end_point = list(map(int, input().split()))
result = []


def go_ahead(now, weight, visited):
    global end_point
    global result
    can_go = node_map[now] # 현재 위치에서 갈 수 있는 섬

    for go, now_weight in can_go:
        if go in visited: # 이미 해당 섬에 방문한 경우
            continue
        go_weight = min(weight, now_weight)
        #visited.add(go)
        if go == end_point:
            result.append(go_weight)
        else:
            visited.add(go)
            go_ahead(go, go_weight, visited)
            visited.remove(go)

go_ahead(start_point, 1000000001, set([start_point]))
print(max(result))
#print(result)
#print(node_map)