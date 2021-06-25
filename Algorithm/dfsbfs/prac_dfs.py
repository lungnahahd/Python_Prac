# dfs 생성 및 그래프 표현 연습 코드

#dfs 메서드 정의
def dfs(graph,v,visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

# 2차원 그래프를 리스트로 표현
# 그래프의 시작을 노드 1부터 시작시키기 위해 처음 인덱스를 비워두기
# 각 인덱스의 리스트로 각 인덱스 번호를 갖는 노드와 인접한 노드들을 표현
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 노드의 방문 여부를 리스트로 표현
# 여기서도 노드를 1부터 시작하기 위해 리스트를 실제 노드보다 하나 더 크게 구현
visited = [False] * 9

dfs(graph,1,visited)
