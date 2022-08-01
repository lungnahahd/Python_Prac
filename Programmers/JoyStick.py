# JoyStick
## 조이스틱을 이동해서 원하는 알파벳 만들기

def solution(name):
    answer = 0
    whereA = []
    beforeA = False
    temp = -1
    # N을 기준으로 이동하기(따악 중간)
    # ord(A) = 65, ord(Z) = 90 , ord(N) = 78
    for idx, word in enumerate(name):
        wordCost = ord(word)
        if wordCost <= 78:
            answer += (wordCost - 65)
            if wordCost == 65:
                if beforeA:
                    whereA.append((temp,idx))
                    beforeA = False
                else:
                    beforeA = True
                    temp = idx
        else:
            answer += (91 - wordCost)
    if beforeA:
        whereA.append((temp,temp))
    ##################################### 여기까지가 알파벳 기준 JoyStick 처리        
    moveCnt = len(name) - 1
    for idx in range(len(whereA)):
        start, end = whereA[idx]
        tempCnt = 0
        if start != 0:
            if end == len(name) - 1:
                tempCnt += (start - 1)
            else:
                tempCnt += (start-1) * 2
        tempCnt += (len(name) - end - 1)
        moveCnt = min(moveCnt,tempCnt)
    answer += moveCnt
    print(moveCnt)
    return answer



#name ="JAN"
name = "JEROEN"
#name = "AAAEASAHQAYTAAAJ" # 60
#name = "AAAABABAAAA"
#name = "JAZ"
#name = "AAIAPB"
print(solution(name))