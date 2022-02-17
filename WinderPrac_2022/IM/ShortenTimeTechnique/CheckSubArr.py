# 부분수열 여부 판단하기
## 두 수열 A와 B가 주어졌을 때 B가 A의 부분수열인지 판단하는 프로그램을 작성해보세요.
## B가 A의 부분수열이라 함은 B의 원소가 차례대로 A의 원소에 존재할 때를 의미합니다.
## 예를 들어 A = [5, 1, 20, 3, 4] 일 때, B = [5, 1, 4] 라면 5 1 4가 차례대로 수열 A에 존재하므로 B는 A의 부분수열입니다. 
## 하지만 만약 A = [5, 1, 20, 3, 4], B = [5, 3, 1] 이라면 5 3 1이 수 열 A에 차례대로 존재하지 않으므로 B는 A의 부분수열이 아닙니다.
### 테크닉 : Two Pointer 테크닉

aSize, bSize = input().split()
aSize,bSize = int(aSize),int(bSize)

aArr = list(map(int,input().split()))
bArr = list(map(int,input().split()))

aIdx = 0
subCheck = True

for i in range(bSize):
    want = bArr[i]
    while aIdx < len(aArr) and aArr[aIdx] != want:
        aIdx += 1
    if aIdx == aSize:
        subCheck = False
        break
    else:
        aIdx += 1

if subCheck:
    print("Yes")
else:
    print("No")