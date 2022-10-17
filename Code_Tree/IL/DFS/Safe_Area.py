# 안전 지대


r_size, c_size = map(int,input().split())
village = []
max_k = -1
for _ in range(r_size):
    temp = input()
    temp = list(map(int,temp.split()))
    max_k = max(max_k,max(temp))
    village.append(temp)



def dfs(k,start_row,start_col):
    global visited
    move = [(+1,0),(0,+1),(-1,0),(0,-1)]
    save = []
    save.append((start_row,start_col))
    result = 1
    visited[start_row][start_col] = True
    while save:
        row,col = save.pop()
        for idx in range(4):
            r,c = move[idx]
            now_row,now_col = r + row, c + col
            if 0 <= now_row < r_size and 0 <= now_col < c_size and village[now_row][now_col] > k and not visited[now_row][now_col]:
                visited[now_row][now_col] = True
                save.append((now_row,now_col))
                result +=1
    return True

result = 0
mid_sum = 0
for k in range(max_k):
    visited = [[False for _ in range(c_size)] for _ in range(r_size)]
    row, col = 0,0
    area_size = 0
    while row != r_size or col != c_size:
        if col == c_size:
            col = 0
        if not visited[row][col] and village[row][col] > k:
            dfs(k,row,col)
            area_size += 1
        col += 1
        if col == c_size:
            row += 1
    if mid_sum < area_size:
        mid_sum = area_size
        result = k
print(result,mid_sum)