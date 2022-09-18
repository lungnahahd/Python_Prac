# 행렬 테두리 회전하기

# 한바퀴씩 돌 때, 방향을 잡아줄 배열
row_move = [1,0,-1,0]
col_move = [0,1,0,-1]

def solution(rows, columns, queries):
    num_arr = [[i*columns + j for j in range(1,columns+1)] for i in range(rows)] # 원본 배열
    answer = []
    for col1,row1,col2,row2 in queries:
        col1,row1,col2,row2 = col1-1,row1-1,col2-1,row2-1
        # 방향을 전환할 기준이 될 점들
        col_check = [col1,col2,col2,col1]
        row_check = [row2,row2,row1,row1]
        before_num, now_way = num_arr[col1][row1] ,0
        small_num = before_num
        col_now,row_now = col1,row1
        while now_way != 4:
            if col_now == col_check[now_way]and row_now == row_check[now_way]: # 방향 전환 조건
                now_way += 1
            else:
                num_arr[col_now+col_move[now_way]][row_now+row_move[now_way]],before_num = before_num,num_arr[col_now+col_move[now_way]][row_now+row_move[now_way]]
                small_num = min(small_num,before_num) # 최소값 갱신
                row_now += row_move[now_way]
                col_now += col_move[now_way]
        
        answer.append(small_num)

    
    return answer


print(solution(6,6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100,97,[[1,1,100,97]]))