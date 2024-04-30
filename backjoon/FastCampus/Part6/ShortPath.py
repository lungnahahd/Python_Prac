import sys
import heapq
INT_MAX = sys.maxsize
input = sys.stdin.readline


cnt_node, cnt_line = list(map(int, input().split()))
start_node = int(input())
path = [[INT_MAX for _ in range(cnt_node+1)] for _ in range(cnt_node+1)]

for _ in range(cnt_line):
    start, end, cost = list(map(int, input().split()))
    path[start][end] = min(path[start][end], cost)

answer = path[start_node]

# for k in range(1, cnt_node+1):
#     for j in range(1, cnt_node+1):
#         if j == start_node:
#             path[start_node][j] = 0
#         else:
#             path[start_node][j] = min(path[start_node][k] + path[k][j], path[start_node][j])

def find_short_path(start_node):
    global answer

    short_q = []
    visited = set()
    visited.add(start_node)
    answer[start_node] = 0
    for idx in range(1, len(answer)):
        heapq.heappush(short_q, (answer[idx], idx))

    while short_q:
        cost, node = heapq.heappop(short_q)
        if node in visited:
            continue
        else:
            if cost > answer[node]:
                continue
            for idx in range(1, len(answer)):
                if idx in visited:
                    continue
                else:
                    if answer[idx] > cost+ path[node][idx]:
                        answer[idx] = cost + path[node][idx]
                        heapq.heappush(short_q, (answer[idx], idx))

find_short_path(start_node)

for cost in answer[1:]:
    if cost == INT_MAX:
        print("INF")
    else:
        print(cost)
