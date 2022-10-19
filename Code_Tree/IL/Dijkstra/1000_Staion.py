# 천 개의 정거장

import heapq
import sys


start,end,bus_num = map(int,input().split())

bus_line = [[] for _ in range(1001)]

big_node = -1
for bus in range(bus_num):
    cost, station_num = map(int,input().split())
    go = list(map(int,input().split()))
    before = -1
    for j in go:
        if before == -1:
            before = j
        else:
            bus_line[before].append([j,bus,cost])
            before = j
        if j > big_node:
            big_node = j

INT_MAX = sys.maxsize
dist = [[INT_MAX,INT_MAX] for _ in range(big_node + 1)]

q = []
visited = [False for _ in range(big_node + 1)]
heapq.heappush(q,(0,start,-1))
visited[start] = True
go = 1
while q:
    cost, now, before_bus = heapq.heappop(q)
    
    for i in bus_line[now]:
        if before_bus == -1:
            if dist[i[0]][0] >= cost + i[2]:
                dist[i[0]][0] = cost + i[2]
                if dist[i[0]][0] == cost + i[2]:
                    dist[i[0]][1] = min(go,dist[i[0]][1])
                else:
                    dist[i[0]][1] = go
                heapq.heappush(q,(cost+i[2],i[0],i[1]))
        else:
            if before_bus != i[1]:
                if dist[i[0]][0] >= cost + i[2]:
                    dist[i[0]][0] = cost + i[2]
                    if dist[i[0]][0] == cost + i[2]:
                        dist[i[0]][1] = min(go,dist[i[0]][1])
                    else:
                        dist[i[0]][1] = go
                    heapq.heappush(q,(cost+i[2], i[0],i[1]))
            else:
                if dist[i[0]][0] >= cost:
                    dist[i[0]][0] = cost
                    if dist[i[0]][0] == cost + i[2]:
                        dist[i[0]][1] = min(go,dist[i[0]][1])
                    else:
                        dist[i[0]][1] = go
                    heapq.heappush(q,(cost,i[0],i[1]))
    go += 1

answer = dist[end]
if answer[0] == INT_MAX:
    print("-1 -1")
else:
    answer[0] = str(answer[0])
    answer[1] = str(answer[1])
    print(" ".join(answer))