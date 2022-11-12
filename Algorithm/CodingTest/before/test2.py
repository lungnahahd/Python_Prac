from enum import Flag
from sqlalchemy import false, true


def solution(n, clockwise):
    minusNum = n -2
    answer = [[0 for _ in range(n)] for _ in range(n//2+1)]
    if n == 1:
        return [[1]]
    else :
        for i in range(1,n):
            answer[0][i-1] = i
        answer[0][n-1] = 1
        count = 2
        row = 1
        while minusNum > 1:
            temp = count
            check = minusNum
            for i in range(n):
                idx = n - i - 1
                if temp != 0:
                    answer[row][idx] = answer[row-1][idx] + 1
                    temp -= 1
                elif check !=0:
                    answer[row][idx] = answer[row-1][idx] + minusNum
                    check -=1
                else:
                    answer[row][idx] = answer[row-1][idx] - 1
            count += 1
            minusNum -= 2
            row += 1
        if n % 2 != 0:
            temp = n//2 + 2
            for i in range(n):
                idx = n - i - 1
                if temp !=0 :
                    answer[n//2][idx] = answer[n//2-1][idx] + 1
                    temp -= 1
                else:
                    answer[n // 2 ][idx] = answer[n // 2 -1][idx] - 1
        else:
            answer.pop()

        row = n//2-1
        while row >= 0:
            tempList = answer[row][:]
            tempList.reverse()
            answer.append(tempList)
            row -= 1
        if clockwise:
            return answer
        else:
            answer.reverse()
            return answer
   

print(solution(6, False))
