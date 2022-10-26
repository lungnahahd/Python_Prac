# 치즈

from collections import deque

move = [[+1,0],[0,+1],[-1,0],[0,-1]]
row, col = map(int,input().split())
plain = []
cnt = 0
for _ in range(row):
    t_list = list(map(int,input().split()))
    cnt += t_list.count(1)
    plain.append(t_list)

def check(r,c):
    result = False
    for idx in range(4):
        n_r, n_c = r + move[idx][0], c + move[idx][1]
        if 0 <= n_r < row and 0 <= n_c < col and plain[n_r][n_c] == 0:        
            result = True
            break
    return result

out_num = 0
case_cnt = 0
visited = [[False for _ in range(col)] for _ in range(row)]
change = []
#print(cnt)
while cnt > 0:
    out_num = 0
    for node in change:
        plain[node[0]][node[1]] = 0
    change = []
    
    save = deque()
    for r in range(row):
        for c in range(col):
            if plain[r][c] == 1 and not visited[r][c]:
                if check(r,c):
                    save.append((r,c))
                    out_num += 1
                    change.append([r,c])
                    visited[r][c] = True
                    break
    while save:
        r,c = save.popleft()
        for idx in range(4):
            n_r, n_c = r + move[idx][0], c + move[idx][1]
            if 0 <= n_r < row and 0 <= n_c < col and not visited[n_r][n_c]:
                if plain[n_r][n_c] == 1:
                    if check(n_r,n_c):
                        save.append((n_r,n_c))
                        change.append([n_r,n_c])
                        visited[n_r][n_c] = True
                        out_num += 1 
    case_cnt += 1
    cnt -= out_num




print(case_cnt)
print(out_num)