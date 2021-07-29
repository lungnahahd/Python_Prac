# 폴로이드 워셜 최단 경로 알고리즘
# 다익스트라 알고리즘은 한 시작점에서만 모든 경로까지 최단경로를 구하는 반면
 
INF = int(1e9) # 무한을 의미하는 값 설정
# 노드의 갯수 및 간선의 갯수를 입력 받기
n = int(input())
m = int(input())
# 2차원 리스트를 모두 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)] # 방법 잘 보기!!!!!!!!!
# 자기 자신으로 가는 비용을 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
#각 간선에 대한 정보를 입력 받아서 그 값으로 리스트 초기화
for i in range(m):
    # x = int(input())
    # y = int(input())
    # val = int(input())
    x,y,val = input().split()
    x = int(x)
    y = int(y)
    val = int(val)
    graph[x][y] = val
# 점화식에 따라서 알고리즘 작성
for i in range(1,n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
# 수행된 결과를 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == "INF":
            print("Infinity", end = " ")
        else : 
            print(graph[i][j], end = " ")
    print(end='\n')

### 참고 코드
    # 폴로이드 워셜 최단 경로 알고리즘
# 다익스트라 알고리즘은 한 시작점에서만 모든 경로까지 최단경로를 구하는 반면
 
# INF = int(1e9) # 무한을 의미하는 값 설정
# # 노드의 갯수 및 간선의 갯수를 입력 받기
# n = int(input())
# m = int(input())
# # 2차원 리스트를 모두 무한으로 초기화
# graph = [[INF] * (n+1) for _ in range(n+1)] # 방법 잘 보기!!!!!!!!!
# # 자기 자신으로 가는 비용을 초기화
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == j:
#             graph[i][j] = 0
# #각 간선에 대한 정보를 입력 받아서 그 값으로 리스트 초기화
# for i in range(m):
#     # x = int(input())
#     # y = int(input())
#     # val = int(input())
#     x,y,val = input().split()
#     x = int(x)
#     y = int(y)
#     val = int(val)
#     graph[x][y] = val
# # 점화식에 따라서 알고리즘 작성
# for k in range(1,n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if graph[i][j] > graph[i][k] + graph[k][j]:
#                 graph[i][j] = graph[i][k] + graph[k][j]
# # 수행된 결과를 출력
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if graph[i][j] == "INF":
#             print("Infinity", end = " ")
#         else : 
#             print(graph[i][j], end = " ")
#     print(end='\n')