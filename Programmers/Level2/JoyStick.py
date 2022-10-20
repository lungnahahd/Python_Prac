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
                if not beforeA:
                    beforeA = True
                    temp = idx
            else:
                if beforeA:
                    whereA.append((temp,idx-1))
                    beforeA = False
        else:
            answer += (91 - wordCost)
            if beforeA:
                whereA.append((temp,idx-1))
                beforeA = False
            
    if beforeA:
        whereA.append((temp,len(name)-1))
    ##################################### 여기까지가 알파벳 기준 JoyStick 처리        
    moveCnt = len(name) - 1
    for idx in range(len(whereA)):
        start, end = whereA[idx]
        tempCnt = 0
        startGo = start - 1
        if startGo <0:
            startGo = 0
        endGo = len(name) - end -1
        if endGo < 0:
            endGo = 0
        moveCnt = min(moveCnt,(endGo*2+startGo),(startGo*2+endGo))
    answer += moveCnt
    return answer



#name ="JAN"
name = "JEROEN"
#name = "AAAEASAHQAYTAAAJ" # 60
#name = "AAAABABAAAA"
#name = "JAZ"
#name = "AAIAPB"
print(solution(name))
