# 쿼드 압축 후 개수 세기

# [col,row]

answer = [0,0]
standard = 0

def solution(arr):
    global answer
    global standard
    standard = len(arr)/2
    if len(arr) == 1:
        if answer[0][0] == 1:
            answer[1] += 1
        else:
            answer[0] += 1
    else:
        if len(arr[0][0]) == 2:
            sum_arr = 0
            for col in arr:
                sum_arr += sum(col)
            answer[0] += 4 - sum_arr
            answer[1] += sum_arr%4
        else:
            standard 


    return answer

print(solution([[1,1],[0,0]]))
# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))