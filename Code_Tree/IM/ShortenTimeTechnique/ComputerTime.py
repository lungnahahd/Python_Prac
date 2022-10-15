# 컴퓨터 이용 시간
## n명의 사람이 컴퓨터를 하려 합니다.
## 컴퓨터에는 1번 부터 순서대로 번호가 매겨져 있고, 컴퓨터 이용 시 남아있는 자리 중 번호가 가장 작은 자리에 앉는 것이 규칙입니다.
## 모든 사람이 기다리지 않고 이용할 수 있는 컴퓨터의 최소 개수와 컴퓨터별로 몇 명의 사람이 그 컴퓨터를 이용하였는지를 구하는 프로그램을 작성해보세요.
### 테크닉 : +1-1 테크닉

import heapq

peopleSize = int(input())

timeTable = []
for i in range(peopleSize):
    start, end = input().split()
    timeTable.append((int(start),i, +1))
    timeTable.append((int(end),i,-1))

timeTable.sort() # 컴퓨터 사용 시간을 시간순으로 정렬

timeDic = dict() # 컴퓨터 사용을 시작하는 사람의 정보를 담기위한 딕셔너리
nowCom = 0 # 만약 남는 컴퓨터가 없다면 다음 컴퓨터를 이용하기 위해 존재하는 변수
result = [0 for i in range(peopleSize)] # 결과를 담는 리스트

comSave = [] # min-heap을 활용해서 만약 빈 컴퓨터가 있다면 저장하기


# 시작시간과 종료시간이 겹치는 경우는 없다고 했으므로 간단하게 경우의 수 생각 가능
for point,idx,value in timeTable:
    if value == 1:
        if len(comSave) == 0:
            nowCom += 1
            timeDic[idx] = nowCom
        else:
            timeDic[idx] = heapq.heappop(comSave)
    else:
        com = timeDic[idx]
        result[idx] = com
        heapq.heappush(comSave, com)
        com = timeDic[idx]
for i in result:
    print(i, end=' ')