# 메뉴 리뉴얼
from itertools import combinations
from collections import Counter
import heapq


def solution(orders, course):
    save = []
    result = []
    total =[] # 전체 조합의 배열을 저장할 부분
    for num in course: # 코스 요리의 개수만큼 전체 반복문 진행
        temp = []
        for i in orders: # 각자의 주문을 리스트로 변환하고 거기서 발생할 수 있는 조합을 찾기
            stop = list(i) 
            stop.sort() # 주문을 알파벳 순으로 정렬 -> 정렬하지 않으면 중복 카운트가 안되는 경우 발생 ..
            temp = list(combinations(stop,num)) # 각 주문에 대해 모든 조합을 뽑아내기
            for j in temp:
                total.append(j)
    save = Counter(total).most_common(len(Counter(total))) # 주문의 중복 빈도수를 배열로 저장
    howLong = 0
    howMany = 0
    checkList = set() # 주문에서 음식의 갯수가 이전에 중복된 것이 있는지를 확인하는 set(중복 여부만 판별하면 되므로 list 보다는 set)

    for get in save:
        tempLong = len(get[0])
        if tempLong == howLong: # 음식의 갯수가 같은 경우
            if howMany == get[1] and get[1] > 1: # 갯수도 같고 빈도수도 같은 경우 결과로 저장
                heapq.heappush(result,''.join(map(str,get[0])))
        else:
            checkList.add(howLong) # 음식의 개수를 저장
            if tempLong in checkList: # 현재 조합에 음식의 갯수가 이전에 있다면 지나가기
                continue
            howLong = tempLong
            howMany = get[1]
            if get[1] > 1: 
                heapq.heappush(result,''.join(map(str,get[0])))
        
        
        
        
    result.sort()  
        
    return result

#a = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
a = ["XYZ", "XWY", "WXA"]
#b = [2,3,5]
b = [2,3,4]
print(solution(a,b))