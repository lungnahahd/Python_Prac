# 거의 최단 경로 (5719)
## 난이도 : 플레티넘 5

import sys
import heapq
import copy
INT_MAX = sys.maxsize
input = sys.stdin.readline


def find_short(paths, start):
    hq = []
    answer = [[INT_MAX, {}] for _ in range(len(paths))]
    answer[start] = [0, {}]
    heapq.heappush(hq, (0, start, set()))
    
    while hq:
        now_cost, now_node, now_hist = heapq.heappop(hq)
        if now_cost > answer[now_node][0]:
            continue
        
        for next_node, next_cost in paths[now_node]:
            temp_cost = now_cost + next_cost
            if answer[next_node][0] >= temp_cost:
                temp_hist = now_hist.copy()
                temp_hist.add((now_node,next_node))
                if answer[next_node][0] == temp_cost:
                    answer[next_node][1] = temp_hist.union(answer[next_node][1])
                else:
                    answer[next_node][0] = temp_cost
                #temp_hist = now_hist.copy()
                #temp_hist.add(next_node)
                    answer[next_node][1] = temp_hist
                heapq.heappush(hq, (temp_cost, next_node, temp_hist))
    return answer

def almost_find_short(paths, start, out_road):
    hq = []
    answer = [INT_MAX for _ in range(len(paths))]
    answer[start] = 0
    heapq.heappush(hq, (0, start))
    while hq:
        now_cost, now_node = heapq.heappop(hq)
        if now_cost > answer[now_node]:
            continue
        
        for next_node, next_cost in paths[now_node]:
            temp_cost = now_cost + next_cost
            if answer[next_node] > temp_cost and (now_node, next_node) not in out_road:
                answer[next_node] = temp_cost
                heapq.heappush(hq, (temp_cost, next_node))
    return answer


final = []

while True:
    cnt_node, cnt_road = list(map(int, input().split()))
    if (cnt_node == 0 and cnt_road == 0):
        for asr in final:
            print(asr)
        break
    start, end = list(map(int, input().split()))
    map_path = [[] for _ in range(cnt_node+1)]
    for _ in range(cnt_road):
        s, e, cost = list(map(int, input().split()))
        map_path[s].append((e, cost))
    mid_result = find_short(map_path, start)
    result = almost_find_short(map_path, start, mid_result[end][1])
    if (result[end] == INT_MAX):
        final.append(-1)
    else:
        final.append(result[end])