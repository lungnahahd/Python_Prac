# 큰 수 만들기

def solution(number, k):
    answer = ''
    intNumL = list(map(int,number))
    fntNum = intNumL[:k]
    bigFnt = max(fntNum)
    if bigFnt < intNumL[k]: # 만약, 앞의 최대가 바로 뒤에오는 최대보다 작을 경우 앞을 전부 제거..
        answer = number[k:]
    else:
        outCount = 0
        for num in fntNum:
            if num == bigFnt:
                answer += str(num)
            else:
                outCount += 1
        while outCount != k:
            # 뒤에 숫자를 어떻게 처리할지 작성 필요...
        









    return answer





n = "1924"
k = 2
print(solution(n,k))