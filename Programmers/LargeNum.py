# 가장 큰 수
## 순서를 재배치해서 가장 큰 수 만들기

import heapq

def solution(numbers):
    answer = ''
    saveNum = []
    for num in numbers:
        sNum = str(num)
        temp = ()
        for idx in range(4):
            if idx >= len(sNum):
                temp += (-0.5,)
                #temp.add(-0.5)
            else:
                n = -int(sNum[idx])
                temp += (n,)
        heapq.heappush(saveNum,temp)
    while saveNum:
        aTemp, bTemp, cTemp, dTemp = heapq.heappop(saveNum)
        tempNum = [aTemp, bTemp, cTemp, dTemp]
        for i in tempNum:
            if i == -0.5:
                break
            else:
                answer += str(-i)

    return answer





i = [3, 30, 34, 5, 9]
print(solution(i))