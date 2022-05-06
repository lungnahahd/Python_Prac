# 메뉴 리뉴얼

import heapq

def solution(orders, course):
    answer = []
    orders.sort(key=len) # 리스트 요소를 길이 순으로 정렬
    countResult = {}
    print(orders)
    for i in range(len(orders)):
        for j in range(i+1,len(orders)):
            temp = ""
            for k in orders[i]:
                if k in orders[j]:
                    temp += k
            if len(temp) in course:
                temp = list(temp)
                temp.sort()
                temp = ''.join(temp)
                if temp in countResult:
                    countResult[temp] += 1
                else:
                    countResult[temp] = 1
    now = list(countResult.items())
    q = []
    for i in now:
        heapq.heappush(q,(-len(i[0]),-i[1],i[0]))
    nowCount = 0
    beforeMax = 0
    print(q)
    while len(q) != 0:
        a = q[0]
        heapq.heappop(q)
        if -a[0] == nowCount:
            if beforeMax <= -a[1]:
                answer.append(a[2])
        else:
            nowCount = -a[0]
            beforeMax = -a[1]
            answer.append(a[2])



    answer = list(set(answer))
    answer.sort()
    return answer

a = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
b = [2,3,5]

print(solution(a,b))