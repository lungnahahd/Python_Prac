# 숫자의 표현

def solution(n):
    answer = 1
    mid = n // 2 + 1
    for start in range(1,mid):
        temp_sum = 0
        while temp_sum <= n :
            if temp_sum == n:
                answer += 1
                break
            temp_sum += start
            start += 1
    return answer