# JoyStick
## 조이스틱을 이동해서 원하는 알파벳 만들기

from tkinter.font import names


def solution(name):
    answer = 0
    nameSize = len(name)
    midName = 0
    if nameSize % 2 == 1:
        midName = nameSize // 2 + 1
    else:
        midName = nameSize // 2

    # N을 기준으로 이동하기(따악 중간)
    # ord(A) = 65, ord(Z) = 90 , ord(N) = 78
    for word in name:
        wordCost = ord(word)
        if wordCost <= 78:
            answer += (wordCost - 65)
        else:
            answer += (91 - wordCost)

    ##################################### 여기까지가 알파벳 기준 JoyStick 처리        
    if "A" not in name: # A 가 아예 없는 경우는 그냥 한 번에 쭉 읽는 것이 가장 단기적 루트
        answer += (nameSize-1)
    else:
        if name[-1] == "A": # 맨 마지막이 A인 경우는 그 전까지만 읽기
            temp = nameSize - 2
        else:
            temp = nameSize - 1
        where = 0
        checkA = False
        startA = 0
        while where < nameSize:
            if name[where] == "A":
                if not checkA:
                    startA = where
                    checkA = True
            elif name[where] != "A" or where == nameSize-1:
                if checkA:
                    if startA != 0:
                        startA = startA-1
                    temp = min(temp, startA*2 + (nameSize-where))
                    #print(temp,name[where],startA)
                    checkA = False
            where += 1       
        answer += temp
        
    if answer < 0:
        answer = 0
    return answer



name ="JAN"
#name = "AAAEASAHQAYTAAAJ" # 60
#name = "AAAABABAAAA"
#name = "JAZ"
#name = "JAN"
#name = "AAIAPB"
print(solution(name))