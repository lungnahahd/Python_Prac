# 피로도
## 완전탐색

import heapq

def solution(k, dungeons):
    answer = 0
    d_order = []
    for dg in dungeons:
        start,cost,end = dg[0],dg[1], dg[0]-dg[1]
        heapq.heappush(d_order,(-end,start,cost))
    
    while k > 0 and d_order:
        _, start, cost = heapq.heappop(d_order)
        if k >= start:
            k -= cost
            answer += 1
    
    
    return answer