# 다익스트라 기본 코드
import heapq

distance = [] # 최단 거리를 기록한 리스트 
graph = [] # 각 노드와 간선의 코스트 정보가 들어있는 리스트

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # 시작 노드에 대해 정보 담기
    distance[start] = 0
    while q:
        dist, now = heapq.heappop() # 가장 최단 거리를 팝!
        if distance[now] < dist:
            continue # 이미 최단 거리로 기록되어 있는 경우는 통과
        for i in graph[now]:
            cost = dist + i[1] # 현재 간선을 거쳐서 갈 수 있는 코스트를 최신화
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))