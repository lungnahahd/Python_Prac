# 방문 길이

def solution(dirs):
    answer = 0
    way = dict() # 해당 방향에 대한 정보를 담는 딕셔너리
    # 3번째 숫자는 다음 숫자 기준 방향을 잡아 주는 것
    # 마지막 숫자는 현재 숫자 기준 방향을 잡아 주는 것
    way["U"] = [-1,0,1,0]
    way["D"] = [1,0,0,1]
    way["L"] = [0,-1,2,3]
    way["R"] = [0,1,3,2]
    # [U,D,R,L] 으로 방문 여부를 확인
    room_map = [[[False,False,False,False] for _ in range(11)] for _ in range(11)]
    start_x,start_y = 5,5
    for dir in dirs:
        move_y,move_x,check_visit,now_visit = way[dir] # 움직이는 방향에 맞는 정보를 빼오기
        temp_y,temp_x = start_y+move_y,start_x+move_x # 정보에 맞게 현재 점을 이동
        if 0 <= temp_x < 11 and 0 <= temp_y < 11:
            if not room_map[temp_y][temp_x][check_visit] and not room_map[start_y][start_x][now_visit]:
                answer += 1
                room_map[temp_y][temp_x][check_visit] = True
                room_map[start_y][start_x][now_visit] = True
            start_x, start_y = temp_x,temp_y

    return answer

print(solution("ULURRDLLU")) # 7
print(solution("LULLLLLLU")) # 7