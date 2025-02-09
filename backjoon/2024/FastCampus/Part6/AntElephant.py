# 개코전쟁 (2325)
## 난이도 : 플레티넘 5

import sys
import heapq
INT_MAX = sys.maxsize
input = sys.stdin.readline

cnt_node, cnt_road = list(map(int, input().split()))
road_map = [[] for _ in range(cnt_node+1)]


def find_short(start):
    answer = [INT_MAX for _ in range(cnt_node+1)]
    hq = []
    answer[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        now_cost, now_node = heapq.heappop(hq)
        if now_cost > answer[now_node]:
            continue
        for next_node, next_cost in road_map[now_node]:
            temp_cost = next_cost + now_cost
            if temp_cost < answer[next_node]:
                answer[next_node] = temp_cost
                heapq.heappush(hq, (temp_cost, next_node))
    return answer

def test(start, get_rid_of):
    answer = [INT_MAX for _ in range(cnt_node+1)]
    hq = []
    answer[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        now_cost, now_node = heapq.heappop(hq)
        if now_cost > answer[now_node]:
            continue
        for next_node, next_cost in road_map[now_node]:
            temp_cost = next_cost + now_cost
            if get_rid_of != (now_node, next_node):

                if temp_cost < answer[next_node] :
                    answer[next_node] = temp_cost
                    heapq.heappush(hq, (temp_cost, next_node))
    return answer

def find_detail_way(start, costs, go_hist, final_sum, visited):
    if start == 1:
        return go_hist
    for next_node, mid_cost in road_map[start]:
        if mid_cost + costs[next_node] == final_sum:
            if next_node not in visited:
                go_hist.append((next_node, start))
                visited.add(next_node)
                find_detail_way(next_node, costs, go_hist, final_sum-mid_cost, visited)

for _ in range(cnt_road):
    a, b, cost = list(map(int, input().split()))
    road_map[a].append((b, cost))
    road_map[b].append((a, cost))

first_answer = find_short(1)
#print(first_answer)
short_visited = []
find_detail_way(cnt_node, first_answer, short_visited, first_answer[-1], set())
rst = 0
for val in short_visited:
    a = test(1, val)
    rst = max(rst, a[-1])
print(rst)