# 겹치는 선분들
## 수직선 위에 1부터 N까지 번호가 매겨진 N개의 선분이 있습니다. 선분 1은 원점에서 시작해서 M(1)만큼 왼쪽 혹은 오른쪽으로 그려집니다
## 선분 2는 선분 1을 그리고 마친 지점에서 시작해서 M(2)만큼 왼쪽 혹은 오른쪽으로 그려집니다. 
## 이런식으로 선분 i는 선분 i-1을 그리고 마친 지점에서 시작해 M(i)만큼 왼쪽 혹은 오른쪽으로 그려집니다.
##  각 선분의 길이와 그려진 방향이 주어질 때, 이 N개의 선분들이 K개 이상 겹치는 곳의 길이 합을 구하는 프로그램을 작성해보세요.
### 테크닉 : +1-1 테크닉

lineCount, want = input().split() 
lineCount = int(lineCount) # 입력 받을 선분
want = int(want) # 원하는 겹치는 개수 

save = []
startPoint = 0
endPoint = 0
for i in range(lineCount):
    end,direct = input().split()
    end = int(end)
    if direct == "R":
        endPoint = startPoint + end
        save.append((startPoint,+1))
        save.append((endPoint,-1))
    else:
        endPoint = startPoint - end
        save.append((endPoint,+1))
        save.append((startPoint,-1))
    startPoint = endPoint

save.sort() # 점들을 정렬하기(해당 점을 기준으로 하기)

resultLen = 0 # 원하는 만큼의 개수에 해당되는 선분들의 부분을 카운트
temp = 0 # 중간마다 선분의 겹침 여부를 기록할 변수
strLen = 0
checkFirst = True
for point,value in save:
    temp += value
    if temp >= want and checkFirst:
        checkFirst = False
        strLen = point
    elif temp < want and not checkFirst:
        checkFirst = True
        distance = point - strLen
        resultLen += distance
print(resultLen)