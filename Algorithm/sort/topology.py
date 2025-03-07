# 위상 정렬
## 방향 그래프에서 사용하는 정렬 방법으로 모든 노드를 방향성에 거스리지 않으면서 순서대로 나열하는 정렬 방식

### 진입 : 해당 노드에서 들어오는 간선
### 진출 : 해당 노드에서 나가는 간선
### Queue를 이용해서 구현하는 것 고려
### 모든 진입 간선의 수가 0인 것을 Queue에 집어 넣고 Queue에서 하나씩 꺼내면서 진행
### 꺼낸 노드에서 나가는 진출 간선을 모두 제거하고 그 과정에서 새롭게 진입 간선이 0인 노드를 큐에 집어 넣기
### 위의 과정에서 큐가 텅 빌 때까지 반복적으로 수행하고 Queue에 들어가는 순서대로 나열하면 바로 위상 정렬

#### 처음에 노드와 간선의 갯수를 입력받고, 차례로 간선을 입력 받기(시작과 끝 점만 입력 받고 코스트는 없음)

import sys
input = sys.stdin.readline

node, line = map(int, input().split())
direction = []
incost = [0 for i in range(line + 1)]
check = [False for i in range(line+1)]
check[0] = True
incost[0] = -1



list = [[] for i in range(node + 1)]
for i in range(line):
    start, end = map(int, input().split())
    list[start].append(end)
    incost[end] += 1

def checkcostzero(a):
    point = []
    global node
    for i in range(1,node + 1):
        if a[i] == 0 and not check[i]:
            point.append(i)
            check[i] = True
    return point

sort_result = []
result = []
result = checkcostzero(incost)
sort_result.append(result[0])

while len(result) != 0:
    point = result.pop()
    while len(list[point]) != 0:
        point_list = list[point].pop()
        incost[point_list] -= 1

    go = checkcostzero(incost)
    result += go
    sort_result += go
    
print(sort_result)

## 참고 코드
# from collections import deque

# # 노드와 간선을 입력 받기
# node, line = map(int, input().split())
# # 모든 노든에 진입 차수를 0으로 지정
# indegree = [0] * (node + 1)
# # 간선의 정보를 담기 위한 배열 생성
# graph = [[] for i in range(node + 1)]

# # 간선의 정보를 입력 받아서 관련 내용을 업데이트 시키는 부분
# for _ in range(line):
#     a, b = map(int, input().split())
#     graph[a].append(b) # (a,b) 간선 내용을 배열에 저장
#     indegree[b] += 1 # 간선을 보고 진입 차수를 1 증가


# def topology(node, cost_list, line_value):
#     result = [] # 위상 정렬의 결과를 담을 배열
#     q = deque() # Queue의 기능을 수행

#     # 처음에 진입차수가 0인 노드를 Queue에 넣기
#     for i in range(1, node + 1):
#         if cost_list[i] == 0:
#             q.append(i)
            
    
#     while q:
#         # Queue에서 하나씩 꺼내고 꺼낸 것은 바로 결과 배열로 넣어주기
#         now = q.popleft()
#         result.append(now)

#         # 방금 Queue에서 꺼낸 노드의 진출 간선을 하나씩 제거하고 그때 진입 차수가 0이 되는 것은 Queue에 넣어주기
#         for i in line_value[now]:
#             cost_list[i] -= 1
#             if cost_list[i] == 0:
#                 q.append(i)
    
#     return result

# print(topology(node,indegree,graph))