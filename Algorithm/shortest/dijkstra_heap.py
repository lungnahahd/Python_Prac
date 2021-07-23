# 기존의 다익스트라 알고리즘은 단계가 진행되면서 길이가 짧은 간선을 계속 찾을 필요 있음
# 기존의 짧은 간선을 찾는 과정에서 정말 많은 시간이 필요
# 이를 보완하고자 힙을 이용
import sys
import heapq
from typing import Sized
input = sys.stdin.readline
INF = int(1e9) # 무한을 나타내는 숫자 표시

save = [] # 추가하는 힙

# 이렇게 입력을 한 번에 여러 개 받을 수 있음에 주의!!
node, line = map(int, input().split())
start = int(input())
distance = []

distance = [INF for _ in range(node+1)] # 방법 잘 보기!!!!!!!!!
check = [False * (node+1) for _ in range(node+1)]
distance[start] = 0

# 이렇게 2차원 리스트 만드는 것 주의해서 보기
graph = [[]for i in range(node+1)]

linecount = []
linecount = [0 for i in range(0, node+1)]
for i in range(line):
    a, b, c = map(int, input().split())
    # 리스트에 대한 정보를 튜플 형식으로 저장
   # graph[a].append((b,c))
   # 최소 힙에 담기 위해서 순서를 변경해서 집어 넣기
    graph[a].append((c,b))
    linecount[a] += 1

def changedistance():
    count = 0
    object = start
    while start == object or len(save) != 0: 
    #count < node:
        #object  = findshort()
        
        if object == -1:
            break
        print(object)
        if not check[object]:
            for i in range(linecount[object]):
                if object == start:
                    if distance[graph[object][i][1]] > graph[object][i][0] + distance[object]:
                        distance[graph[object][i][1]] = graph[object][i][0] + distance[object]
                        heapq.heappush(save, graph[object][i])
                    
                else:
                    if len(save) == 0:
                        break
                    else:
                    #object = heapq.heappop(save)[1]
                        if check[object]:
                            continue
                        else:
                            if distance[graph[object][i][1]] > graph[object][i][0] + distance[object]:
                                distance[graph[object][i][1]] = graph[object][i][0] + distance[object]
                                heapq.heappush(save, graph[object][i])
                            else:
                                heapq.heappush(save,graph[object][i])
        count +=1
        check[object] = True
        object = heapq.heappop(save)[1]
        if len(save) == 0:
            break
        

changedistance()
print(distance)