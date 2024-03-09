# 효율적인 해킹 (1325)
## 난이도 : 하

### 해당 문제는 pypy로 제출...
## bfs는 원체 시간이 많이 걸리는 느낌이라 이와 같이 해결 

import sys
from collections import deque

input = sys.stdin.readline

cnt_computer, cnt_believe = list(map(int, input().split()))

computer = [[] for _ in range(cnt_computer+1)]
result = [0 for _ in range(cnt_computer+1)]


# Node를 모두 방문하기 위해 조금 더 시간복잡도에서 효과적인 bfs를 활용
def bfs(start, visited):
    go = deque([start])
    make_disease = 0
    visited[start] = True
    while go:
        now_com = go.popleft()
        
        for next_com in computer[now_com]:
            if visited[next_com]:
                continue
            visited[next_com] = True
            go.append(next_com)
            make_disease += 1    
    return make_disease

# 간선에 대한 정보
for _ in range(cnt_believe):
    a_com, b_com = list(map(int, input().split()))
    computer[b_com].append(a_com) # b 컴퓨터가 감염되면, a 컴퓨터가 감염

for idx in range(1, cnt_computer+1):
    visited = [False for _ in range(cnt_computer+1)]
    result[idx] = bfs(idx, visited)

big_num = max(result)
answer = []

# 결과를 출력할 부분
for idx in range(1, cnt_computer+1):
    if (result[idx] == big_num):
        answer.append(str(idx))
print(' '.join(answer))