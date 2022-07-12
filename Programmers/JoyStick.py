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
    where = 0
    # N을 기준으로 이동하기(따악 중간)
    # ord(A) = 65, ord(Z) = 90 , ord(N) = 78
    for word in name:
        wordCost = ord(word)
        if wordCost <= 78:
            answer += (wordCost - 65)
        else:
            answer += (91 - wordCost)

  
    frontWhere, backWhere = midName - 1, midName
    answer += (midName -1)
    answer += (nameSize - midName )
   
    while frontWhere >= 0:
        if name[frontWhere] == "A":
            if answer == 0:
                break
            answer -= 1
            frontWhere -= 1
        else:
            break
    while backWhere < len(name):
        if name[backWhere] == "A":
            if answer == 0:
                break
            answer -= 1
            backWhere += 1
        else:
            break


    return answer




name = "AAAAA"
#name = "JAZ"
#name = "JAN"
print(solution(name))