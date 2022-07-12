# JoyStick
## 조이스틱을 이동해서 원하는 알파벳 만들기

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



            
    if "A" not in name:
        answer += (nameSize-1)
    else:
        if name[-1] == "A":
            temp = nameSize - 2
        else:
            temp = nameSize - 1
        where = 1
        seqA = [False, 0]
        checkA = 0
        while where < nameSize:
            if name[where] == "A":
                if seqA[0]:
                    temp = min(temp, (seqA[1]-1)*2 + (nameSize-1-where))

                else:
                    seqA[0] = True
                    seqA[1] = where
                    temp = min(temp, (where-1)*2 + (nameSize-1-where) )
            else:
                seqA[0] = False
            where += 1
        answer += temp
    if answer < 0:
        answer = 0
    return answer




name = "AAAEASAHQAYTAAAJ" # 60
name = "AAAABABAAAA"
#name = "JAZ"
#name = "JAN"
#name = "AAIAPB"
print(solution(name))