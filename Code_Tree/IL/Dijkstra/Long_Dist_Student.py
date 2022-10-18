import heapq
import sys

place, road = map(int,input().split())
school = place
time = [[] for _ in range(place+1)]
for _ in range(road):
    end,start,weight = map(int,input().split())
    time[start].append([end,weight])

INT_MAX = sys.maxsize
distance = [INT_MAX for _ in range(place+1)]

def find(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for go in time[now]:
            cost = go[1] + dist
            if cost < distance[go[0]]:
                distance[go[0]] = cost
                heapq.heappush(q,(cost,go[0]))
find(school)
print(max(distance[1:]))