# 2xN 타일링

answer = 0

def solution(n):
    temp_save = [0,1,2]
    if n > 2:
        for i in range(3,n+1):
            sum_num = temp_save[i-2] + temp_save[i-1] % 1000000007
            temp_save.append(sum_num)
    return temp_save[n]

print(solution(4)) # 5
print(solution(5))