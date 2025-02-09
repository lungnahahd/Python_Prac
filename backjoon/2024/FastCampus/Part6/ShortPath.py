# 최딘경로 (1753)
## 난이도 : 골드 4

import sys
import heapq
INT_MAX = sys.maxsize
input = sys.stdin.readline


cnt_node, cnt_line = list(map(int, input().split()))
start_node = int(input())
path = [[] for _ in range(cnt_node+1)]

for _ in range(cnt_line):
    start, end, cost = list(map(int, input().split()))
    path[start].append((cost, end))

answer = [INT_MAX for _ in range(cnt_node + 1)]


def find_short_path(start_node):
    global answer

    short_q = []
    answer[start_node] = 0
    #visited = set()
    #visited.add(start_node)
    # for cost, end in path[start_node]:
    #     heapq.heappush(short_q, (cost, end))

    heapq.heappush(short_q, (0, start_node))

    while short_q:
        cost, node = heapq.heappop(short_q)
        
        if cost > answer[node]:
            continue

        answer[node] = cost
        #visited.add(node)

        for c,e in path[node]:
            temp = cost + c
            if temp < answer[e]:
                answer[e] = temp
                heapq.heappush(short_q, (temp, e))

        

find_short_path(start_node)

for cost in answer[1:]:
    if cost == INT_MAX:
        print("INF")
    else:
        print(cost)

# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6