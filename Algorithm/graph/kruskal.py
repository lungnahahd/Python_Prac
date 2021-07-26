# 크루스컬 알고리즘
# 신장트리 관련 알고리즘으로 그리디 알고리즘의 성격을 포함
# 간선을 확인하면서 이를 포함시킬지 말지를 결정
# 비용에 따라서 오름차순 정렬하여서 비용이 적은 간선부터 확인
# 현재 간선이 사이클을 형성한다면 포함시키지 않고, 사이클을 형성하지 않는다면 포함

# 처음에는 점과 간선의 갯수 입력을 받고 차례대로 출발점, 도착점, 코스트를 입력 받기

import heapq
import pdb
import sys
from types import DynamicClassAttribute
input = sys.stdin.readline
INF = int(1e9)

node, line = map(int, input().split())
result = 0
cycle = False

paranet = []
paranet.append(0)
for i in range(1, node+1):
    paranet.append(i)


distance = []
for i in range(line):
    a, b, c = map(int, input().split())
    heapq.heappush(distance,(c,[a,b]))

def FindParanet(child):
    if paranet[child] == child:
        return child
    else:
        return FindParanet(paranet[child])

def Union(start, end):
    if paranet[start] < paranet[end]:
        paranet[end] = paranet[start]
    else:
        paranet[start] = paranet[end]

while len(distance) != 0:
    get = heapq.heappop(distance)
    if FindParanet(get[1][0]) == FindParanet(get[1][1]):
    #if FindParanet(heapq.heappop(distance)[1][0]) == FindParanet(heapq.heappop(distance)[1][1]) :
        continue
    else :
        Union(get[1][0], get[1][1])
        result += get[0]
        # Union(heapq.heappop(distance)[1][0], heapq.heappop(distance)[1][1])
        # result += heapq.heappop(distance)[0]

print(result)

# print(heapq.heappop(distance)[1][0]) # 출발점을 나타내는 코드