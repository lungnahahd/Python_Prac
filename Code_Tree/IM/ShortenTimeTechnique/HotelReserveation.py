# 호텔 예약
## 테크닉 : +1-1 테크닉


# 입력이 크다는 가정하에 배열로 한다면 메모리 관련 문제가 발생
peoples = int(input())
dayCheck = []

for i in range(peoples):
    startD,endD = input().split()
    startD = int(startD)
    endD = int(endD)
    dayCheck.append((startD,+1))
    dayCheck.append((endD,-1))

dayCheck.sort()
#print(dayCheck)

result  = 0
temp = 0
count = 0
for point,value in dayCheck:
    # 한 명이 나가고 해당 날에 다른 사람이 들어오는 경우에도 겹치는 것으로 인정해서 해당 부분을 처리해주는 코드
    if count+1 < len(dayCheck):
        pointAfter,valueAfter = dayCheck[count+1]
        if pointAfter == point:
            result = max(result, temp + valueAfter)
            temp += value

        else:
            temp += value
            result = max(result,temp)
    else:
        temp += value
        result = max(result,temp)
    count += 1
print(result)