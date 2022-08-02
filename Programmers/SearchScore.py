# 순위 검색
## 아이디어 -> 점수 순으로 heap에 담고, 나머지 조건은 set으로 구성해서 빠르게 검색이 가능하도록 하기

import heapq
from unittest import result

def solution(info, query):
    answer = []
    score =[]
    for i in info:
        temp = i.split(' ')
        save = set()
        for j in temp[:-1]:
            save.add(j)
        heapq.heappush(score,(-int(temp[-1]),save))
###################### score 순으로 조건이 들어있는 set과 함께 저장 완료########################
    for q in query:
        temp = q.split(' ')
        count = 0
        #here = True
        for idx in range(len(score)):
            here = True
            if -score[idx][0] >= int(temp[-1]): # 점수를 먼저 비교
                nowPle = score[idx][1]
                for i in range(0,8,2):
                    if temp[i] == "-":
                        continue
                    else:
                        if temp[i] not in nowPle:
                            here = False
                            break
                if here:
                    count  += 1
            else:
                break
        answer.append(count)





    return answer

i = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
q = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(i,q))