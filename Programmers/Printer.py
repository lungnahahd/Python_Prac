# 프린터(Level 2)
## 우선 순위에 따른 출력 프린터
## 숫자가 클수록 우선 순위가 높음

import heapq

def solution(priorities, location):
    answer = 0
    qPriority = [] # 우선 순위를 담는 큐
    strTemp = "" # 리스트 대신 문자열로 간편하게 처리
    iNowPlace = location # 출력을 원하는 문서 위치를 표시
    iSize = 0 # 반복문을 멈출 용도 -> 솔직히 필요는 없는 변수
    for paper in priorities: 
        heapq.heappush(qPriority, -paper) # 인쇄 목록에서 하나씩 빼서 우선순위 Queue에 넣기
        strTemp += str(paper) # 리스트를 문자열로 변환
    while iSize < len(priorities):
        if -qPriority[0] == int(strTemp[0]): # 현재 인쇄물을 출력해야 되는 경우
            iSize += 1
            if iNowPlace == 0:
                answer = iSize
                break
            heapq.heappop(qPriority) 
            strTemp = strTemp[1:] # 인쇄물을 목록에서 제거
        else: # 인쇄물을 뒤로 보내야되는 경우
            strTemp = strTemp[1:] + strTemp[0]
        iNowPlace -= 1 # 인쇄물이 뒤로 가면서 원하는 인쇄물의 위치를 갱신
        if iNowPlace < 0:
            iNowPlace = len(strTemp) - 1
        

    return answer








lstPriority = [2,1,3,2]
iLocation = 2
# lstPriority = [1, 1, 9, 1, 1, 1]
# iLocation = 0
print(solution(lstPriority, iLocation))


