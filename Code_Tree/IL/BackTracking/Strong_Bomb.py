# 강력한 폭발

size  = int(input())
area = []
for i in range(size):
    temp = list(map(int,input().split()))
    area.append(temp)
bombs = []
row_move = [[-2,-1,+1,+2],[0,0,-1,+1],[-1,+1,-1,+1]]
col_move = [[0,0,0,0],[-1,+1,0,0],[-1,-1,+1,+1]]

# 폭탄 위치 찾기
for i in range(size):
    for j in range(size):
        if area[i][j] == 1:
            bombs.append((i,j))
bomb_num = len(bombs)
die_area = -1
temp = []

def dt():
    global bombs
    global die_area

    for i in range(3):
        if len(temp) == bomb_num:
            now_die = 0
            visited = [[0 for _ in range(size)] for _ in range(size)]
            for i in range(bomb_num):
                now_row,now_col = bombs[i]
                if visited[now_row][now_col] == 0:
                    now_die += 1
                    visited[now_row][now_col] = 1
                for j in range(4):
                    temp_row,temp_col = row_move[temp[i]][j] + now_row,col_move[temp[i]][j] + now_col
                    if 0 <= temp_row < size and 0 <= temp_col < size and visited[temp_row][temp_col] == 0:
                        visited[temp_row][temp_col] = 1
                        now_die += 1

            die_area = max(die_area,now_die)
            return
        else:
            temp.append(i)
            dt()
            temp.pop()
dt()
print(die_area)