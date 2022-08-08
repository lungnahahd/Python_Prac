# 큰 수 만들기

import math

def solution(number, k):
    answer = ''
    intNumL = list(map(int,number))
    saveBox = []
    before = intNumL[0]
    idx = 0
    for num in intNumL:
        if k == 0 or num == before:
            saveBox.append(num)
        elif num > before:
            k -= 1
            saveBox.pop()
            saveBox.append(num)
            before = num
        else:
            ################ 이 부분 처리 필요....
            ## 즉, 마지막 케이스의 4,7 을 처리하는 경우와 7,5를 처리하는 경우를 다리게 하기
            if saveBox[-1] >= num:
                saveBox.append(num)
                before = num
            else:
                k -= 1
    if k != 0:
        saveBox = saveBox[:len(saveBox) - k]

    answer = saveBox

    return answer





n = "4177252841"
k = 4
print(solution(n,k))
