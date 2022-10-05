# 방문 길이

def solution(dirs):
    answer = 0
    way = dict()
    # 마지막 숫자는 다음 숫자 기준 방향을 자방 주는 것
    way["U"] = [0,1,1]
    way["D"] = [0,-1,0]
    way["L"] = [-1,0,2]
    way["R"] = [1,0,3]
    # [U,D,R,L] 으로 방문 여부를 확인
    room_map = [[[False,False,False,False] for _ in range(11)] for _ in range(11)]
    start_x,start_y = 5,5
    for dir in dirs:
        move_x,move_y,check_visit = way[dir]
        temp_x,temp_y = start_x+move_x,start_y+move_y
        if 0 <= temp_x < 11 and 0 <= temp_y < 11:
            if not room_map[temp_y][temp_x][check_visit]:
                answer += 1
                room_map[temp_y][temp_x][check_visit] = True
            start_x, start_y = temp_x,temp_y

    return answer

print(solution("ULURRDLLU")) # 7
print(solution("LULLLLLLU")) # 7