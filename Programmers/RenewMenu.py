# 메뉴 리뉴얼
from itertools import combinations
import heapq


def solution(orders, course):
    save = []
    count = 0
    for num in course: # 코스 요리의 개수만큼 전체 반복문 진행
        temp = []
        for i in orders: # 각자의 주문을 리스트로 변환하고 거기서 발생할 수 있는 조합을 찾기 
            temp.append(list(combinations(list(i),num)))
            many = 0
        for now in temp: # 각 주문의 조합을 꺼내기
            for get in now: # 주문의 조합을 하나씩 확인
                middle = 0
                if count + 1 == len(temp):
                    break
                for check in temp[count+1:]: # 조합이 다른 주문에 있는지 여부를 확인
                    if get in check:
                        middle += 1
                if middle >= many:
                    heapq.heappush(save,(-many,get))

    print(save)


            
    answer = []
    return answer

a = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
b = [2,3,5]

print(solution(a,b))