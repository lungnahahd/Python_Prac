# 124 나라의 숫자(Level 2)

def solution(n):
    answer = ''
    numArr = [4,1,2,4]
    check = False
    while n > 3:
        temp = n % 3
        n = n // 3
        if check:
            temp -= 1
            check = False
        answer = str(numArr[temp]) + answer
        if temp == 0:
            check = True
    if check:
        n -= 1
    answer = str(numArr[n]) + answer


    return answer


print(solution(115))