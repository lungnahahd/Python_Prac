## 기능 개발

import math

def solution(progresses, speeds):
    answer = [] # 기능 배포들의 수를 담는 경우의 수
    count = 1 # 현재가 몇 일째인지를 담는 변수
    today = 0 # 오늘 한 번에 배포할 기능이 몇 개인지 계속적으로 카운트 해주는 변수
    for i in range(len(progresses)):
        remainder = 100 - progresses[i] # 현재 작업의 남은 날짜를 체크
        if remainder <= speeds[i] * count: # 작업이 현재 배포 가능하면 바로 오늘 배포 작업에 추가해주기
            today += 1
            continue
        else: # 현재 해당 작업이 배포되지 못하는 경우 동작
            if today != 0: # 기존에 카운트 되던 값은 바로 배열에 넣어주기
                answer.append(today)
                today = 0
            count = math.ceil((remainder / (speeds[i])))
            today += 1
            
    if today != 0:
        answer.append(today)

    return answer


#p = [93, 30, 55]
#s = [1, 30, 5]

#p = [95, 90, 99, 99, 80, 99]
#s = [1, 1, 1, 1, 1, 1]

#p =[90, 90, 90]
#s = [1, 1, 1]

print(solution(p,s))