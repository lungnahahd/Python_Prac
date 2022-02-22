# 최소 통과 시간
## n개의 물건을 m개의 통로를 통해 통과시키려 합니다.
## m개의 통로를 통과하는데 걸리는 시간이 각각 다를 때, n개의 물건을 모두 통과시키는데 걸리는 최소 시간을 구하는 프로그램을 작성해보세요
## 단, 통로에 물건이 이동하고 있다면 그동안 다른 물건은 그 통로로 들어가지 못합니다.
### 테크닉 : 이진 탐색 응용

import sys
INT_MAX = sys.maxsize


n, m = input().split()
thingCount, acessCount = int(n),int(m)

timeTable = []
for i in range(acessCount):
    get = int(input())
    timeTable.append(get)

timeTable.sort()

left = 0
right = thingCount * timeTable[acessCount -1] # 답이 될 수 있는 최대 시간 -> 전부 오래 걸리는 것으로 통과

ans = INT_MAX # 정답을 기록하는 변수

# 걸리는 시간을 넘기면, 해당 시간에는 원하는 물건을 전부 통과시킬 수 있는지를 판별하는 함수
def check(num):
    count = 0
    for i in timeTable:
        count += num // i
    if count >= thingCount:
        return True
    else:
        return False

# 이진탐색을 활용하는 부분
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = min(mid,ans)
        right = mid - 1
    else:
        left = mid + 1
print(ans)