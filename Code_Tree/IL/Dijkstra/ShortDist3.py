# 최단거리 3
import sys
import heapq
input = sys.stdin.readline

INT_MAX = sys.maxsize

node_cnt, line_cnt = list(map(int, input().split()))
graph = [[] for _ in range(node_cnt+1)]

cost = [INT_MAX for _ in range(node_cnt + 1)]

for idx in range(line_cnt):
    node1, node2, value = list(map(int, input().split()))
    graph[node1].append((node2, value))
    graph[node2].append((node1, value))
start_node, end_node = list(map(int, input().split()))

cost[start_node] = 0
save = []
heapq.heappush(save, (0, start_node))

while save:
    value, node = heapq.heappop(save)
    for next_node, go_value in graph[node]:
        if cost[next_node] > go_value + value:
            cost[next_node] = go_value + value
            heapq.heappush(save, (go_value + value, next_node))
            
print(cost[end_node])