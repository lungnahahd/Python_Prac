# 부분 수열의 합이 K
## n개의 정수로 이루어진 수열에서 연속된 구간의 합을 구하려합니다.
## 모든 연속된 구간의 합 중에서 합이 k인 것의 개수를 구하는 프로그램을 작성해보세요.
### 테크닉 : 부분합(prefix) 테크닉

cmd = list(map(int, input().split()))

numList = list(map(int,input().split()))
prefix = [0]

sumNum = 0
for i in numList:
    sumNum += i
    prefix.append(sumNum)

count = 0
if prefix[2] == cmd[1]:
    count += 1
for i in range(3,cmd[0]+1):
    if cmd[1] == (prefix[i] - prefix[i-2]):
        count += 1
print(count)