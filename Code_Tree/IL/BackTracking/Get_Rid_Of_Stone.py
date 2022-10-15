# 돌 잘 치우기

from collections import deque

area_size, start_size, out_size = list(map(int,input().split()))

area = []
for _ in range(area_size):
    temp = list(map(int,input().split()))
    area.append(temp)
stone = []

# 돌의 위치를 선택
for i in range(area_size):
    for j in range(area_size):
        if area[i][j] == 1:
            stone.append((i,j))

start_node = []
# 시작점 담기
for _ in range(start_size):
    row,col = list(map(int,input().split()))
    start_node.append((row,col))



row_move = [+1,0,-1,0]
col_move = [0,+1,0,-1]

# 들어갈 수 있는 최대 크기를 계산해주는 bfs 활용
def bfs():
    visited = [[False for _ in range(area_size)] for _ in range(area_size)]
    can_visit = 0
    for idx in range(start_size):
        save = deque()
        row, col = start_node[idx]
        row, col = row - 1, col -1
        if not visited[row][col]:
            visited[row][col] = True
            can_visit += 1
        save.append((row,col))
        while save:
            n_row,n_col = save.popleft()
            for move in range(4):
                m_row,m_col = n_row + row_move[move], n_col + col_move[move]
                if 0 <= m_row < area_size and 0 <= m_col < area_size and area[m_row][m_col] == 0 and not visited[m_row][m_col]:
                    visited[m_row][m_col] = True
                    can_visit += 1
                    save.append((m_row,m_col))

    return can_visit

out_stone = 0
answer = 0

# 백트래킹으로 폭탄 제거를 하는 함수
def dt():
    global out_stone
    global answer
    if out_size == 0:
        temp = bfs()
        answer = temp
        return
    else:
        for idx in range(len(stone)):
            if out_stone == out_size:
                temp = bfs()
                answer = max(answer, temp)
                return
            else:
                n_row, n_col = stone[idx]
                if area[n_row][n_col]:
                    out_stone += 1
                    area[n_row][n_col] = 0
                    dt()
                    out_stone -= 1
                    area[n_row][n_col] = 1


dt()
print(answer)