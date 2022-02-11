# 차이가 가장 작은 수
## n개의 정수로 이루어진 수열에서 두 수를 골랐을 때, 그 차이가 m 이상이면서 제일 작은 경우의 그 차이를 구하는 프로그램을 작성해보세요.
### TreeSet 사용 이유 : 각 위치에 있을 떄, 가장 가깝게 크고, 가장 가깝게 작은 수를 빠르게 선택해야 되므로 사용

import sys
INT_MAX = sys.maxsize
from sortedcontainers import SortedSet

s = SortedSet()      # treeset

cmd = list(map(int,input().split()))

result = INT_MAX
for i in range(cmd[0]):
    num = int(input())
    bigNum = num + cmd[1]
    smallNum = num - cmd[1]
    bigIdx = s.bisect_left(bigNum)
    smallIdx = s.bisect_right(smallNum) - 1
    if smallIdx < 0 and bigIdx == len(s) : 
        s.add(num)
        continue
    elif bigIdx == len(s):
        temp = num - s[smallIdx]
    elif smallIdx < 0:
        temp = s[bigIdx] - num
    else:
        smallTemp = num - s[smallIdx]
        bigTemp = s[bigIdx] - num
        temp = min(smallTemp,bigTemp)
    if result > temp:
        result = temp
    s.add(num)
if result == INT_MAX:
    print(-1)
else:
    print(result)