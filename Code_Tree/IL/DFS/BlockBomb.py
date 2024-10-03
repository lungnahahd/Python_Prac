# 뿌요뿌요
## 상하좌우로 연결된 숫자가 동일하면 카운트
## 카운트가 4이상이면 해당 영역은 파괴
### 파괴된 영역의 개수와 가장 넓은 영역의 크기를 출력
##### dfs를 이용해서 해당 문제를 해결


import sys
input = sys.stdin.readline

map_size = int(input())
r_move=[1,0,-1,0]
c_move=[0,1,0,-1]
visited = [[False for _ in range(map_size)] for _ in range(map_size)]
place = []
num = set()

for r_idx in range(map_size):
    temp = list(map(int, input().split()))
    place.append(temp)

    for c_idx in range(map_size):
        num.add(temp[c_idx])
answer = 0
block = 0
def dfs(num, row, col, cnt):
    global visited, tempSize

    for idx in range(4):
        next_row, next_col = row + r_move[idx], col + c_move[idx]
        if 0 <= next_row < map_size and 0 <= next_col < map_size:
            if not visited[next_row][next_col] and place[next_row][next_col] == num:
                visited[next_row][next_col] = True
                dfs(num, next_row, next_col, cnt + 1)
                tempSize += 1

for r_idx in range(map_size):
    for c_idx in range(map_size):
        if not visited[r_idx][c_idx]:
            visited[r_idx][c_idx] = True
            tempSize = 1
            dfs(place[r_idx][c_idx], r_idx, c_idx, 1)
            answer = max(answer, tempSize)
            if tempSize >= 4:
                block += 1
print(block, answer)