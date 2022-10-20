# 삼각 달팽이

def solution(n):
    answer = []
    total_save = [[0] * n for _ in range(n)] # 전체 구조를 담은 배열
    move_col = [1,0,-1] # 열 이동 
    move_row = [0,1,-1] # 행 이동
    change_way = n  # 방향 전환을 위한 카운트 느낌의 변수
    how_many = 0 # 몇 번 방향 전환 했는가?
    row = 0 # 시작 열
    col = 0 # 시작 행
    num = 1 # 입력 숫자
    while True:
        total_save[col][row] = num
        num += 1
        change_way -= 1
        if change_way == 0: # 방향 전환 조건
            how_many += 1
            change_way = n - how_many
            if change_way == 0: # 종료 조건(더 이상 이동 불가 경우)
                break
        col += move_col[how_many%3]
        row += move_row[how_many%3]
    # 결과 출력 반복문
    for temp in total_save:
        for move_num in temp:
            if move_num == 0:
                break
            answer.append(move_num)




    return answer

print(solution(4))
print(solution(5))
print(solution(6))