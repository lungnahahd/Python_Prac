# 플로이드워셜 틀

INF = int(1e9) # 무한을 의미하는 변수 설정
node = 0 # 노드의 개수
line = 0 # 간선의 개수

graph = [[INF] * (node + 1) for _ in range(node+1)] # 모든 간선을 무한의 값을 갖는 것으로 해서 그래프 생성

for i in range(1,node+1):
    for j in range(1,node+1):
        if i == j:
            graph[i][j] = 0 # 자기 자신을 향하는 경우는 0

#####
# 해당 부분에는 간선의 가중치 입력을 받아 갱신하는 부분 추가 
#####

# 플로이드 워셜 알고리즘의 가장 핵심적인 부분
for k in range(1,node + 1):
    for i in range(1, node+1):
        for j in range(1, node+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    
