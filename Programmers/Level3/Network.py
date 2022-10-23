# 네트워크
## DFS 유형

def solution(n, computers):
    answer = 0
    conn = [[] for _ in range(n)]
    for idx,computer in enumerate(computers):
        for i, val in enumerate(computer):
            if i == idx:
                continue
            if val == 1:
                conn[idx].append(i)

    visited = [False for _ in range(n)]
    can_go = []
    for start in range(n):
        if visited[start]:
            continue
        can_go.append(start)
        visited[start] = True

        
        while can_go:
            node = can_go.pop()
            now = conn[node]
            for i in now:
                if visited[i]:
                    continue
                can_go.append(i)
                visited[i] = True
        
        answer += 1
    
    return answer