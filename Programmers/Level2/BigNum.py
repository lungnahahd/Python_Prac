# 큰 수 만들기

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
            while k != 0 :
                if saveBox[-1] < num:
                    k -= 1
                    saveBox.pop()
                    if len(saveBox) == 0:
                        break
                else:
                    break
            saveBox.append(num)
            before = num
        else:
            saveBox.append(num)
            before = num
       
    if k != 0:
        saveBox = saveBox[:len(saveBox) - k]
    for i in saveBox:
        answer += str(i)

    return answer





n = "4177252841"
k = 4
print(solution(n,k))
