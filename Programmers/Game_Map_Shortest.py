# 게임 맵 최단거리

# (행, 열)

row_move = [-1,+1,0,0]
col_move = [0,0,+1,-1]
go_dist = []

def solution(maps):
    global go_dist
    go_dist = []
    max_row, max_col = len(maps)-1,len(maps[0])-1 # 적팀 진영의 위치
    visited = set() # 방문 여부를 저장할 딕셔너리
    find_way(maps,0,0,1,visited)

    if len(go_dist) == 0:
        return -1
    else:
        return(min(go_dist))
    print(go_dist)

    return answer

def find_way(map,row,col,distance,visited):
    global go_dist
    for cnt in range(4):
        row_temp = row_move[cnt] + row
        col_temp = col_move[cnt] + col
        if 0<=row_temp<len(map) and 0<=col_temp < len(map[0]) and map[row_temp][col_temp] == 1:
            if (row_temp,col_temp) not in visited:
                now_visit = visited.copy()
                now_dist = distance
                now_dist += 1
                now_visit.add((row_temp,col_temp))
                if row_temp == (len(map)-1) and col_temp == (len(map[0])-1):
                    go_dist.append(now_dist)
                find_way(map,row_temp,col_temp,now_dist,now_visit)



# 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

# -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))