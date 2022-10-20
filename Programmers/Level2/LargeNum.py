# 가장 큰 수
## 순서를 재배치해서 가장 큰 수 만들기

def solution(numbers):
    answer = ''
    sNums = []
    for num in numbers:
        sTemp = str(num)
        sNums.append(sTemp * 3)
    sNums.sort(reverse=True)
    #print(sNums)
    for sNum in sNums:
        bigSize = len(sNum)
        size = bigSize // 3
        #print(size)
        answer = answer + sNum[:size]
    if int(answer) == 0:
        return '0'    
    return answer


i = [101, 10, 232, 23]
print(solution(i))