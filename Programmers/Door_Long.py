# 방문 길이

def solution(dirs):
    answer = 0
    way = dict()
    way["U"] = [0,1,1]
    way["D"] = [0,-1,0]
    way["L"] = [-1,0,3]
    way["R"] = [1,0,2]
    # [U,D,R,L]
    room_map = [[[False,False,False,False] for _ in range(11)] for _ in range(11)]
    start_x,start_y = 5,5
    for dir in dirs:
        move_x,move_y,check_visit = way[dir]
        temp_x,temp_y = start_x+move_x,start_y+move_y
        if 0 <= temp_x < 10 and 0 <= temp_y < 10:
            if not room_map[temp_x][temp_y][check_visit]:
                answer += 1
                room_map[temp_x][temp_y][check_visit] = True
            start_x, start_y = temp_x,temp_y

    return answer

print(solution("ULURRDLLU")) # 7
print(solution("LULLLLLLU")) # 7