# 단지 번호 붙이기 (2667)
## 난이도 : 실버 1

from collections import deque

n = int(input())
villege, answer = [], []
cnt_villege = 0
visited = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    villege.append(list(input()))

def bfs(x,y):
    global visited, villege
    result = 1
    move_x, move_y = [-1,0,+1,0], [0,+1,0,-1]
    stack = deque([(x,y)])
    visited[x][y] = True
    while stack:
        now_x, now_y = stack.popleft()
        for idx in range(4):
            next_x, next_y = now_x + move_x[idx], now_y + move_y[idx]
            if 0 <= next_x < n and 0 <= next_y < n:
                if not visited[next_x][next_y] and villege[next_x][next_y] == '1':
                    result += 1
                    visited[next_x][next_y] = True
                    stack.append((next_x, next_y))

    return result

for x in range(n):
    for y in range(n):
        if not visited[x][y] and villege[x][y] == '1':
            cnt_villege += 1
            answer.append(bfs(x,y))

answer.sort()
print(cnt_villege)
for rst in answer:
    print(rst)