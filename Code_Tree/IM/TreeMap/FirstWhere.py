## n개의 숫자가 주어졌을 때, 각 숫자마다 처음으로 주어진 위치를 구하는 프로그램을 작성해보세요.
### TreeSet 사용 이유 : 숫자의 처음 위치를 확인하고, 이를 오름차순으로 출력해야하므로 사용

from sortedcontainers import SortedDict

countDic = SortedDict()      # treemap

sizeNum = int(input())
numS = list(map(int, input().split()))

for i in range(sizeNum):
    if numS[i] not in countDic:
        countDic[numS[i]] = i+1
    # countDic[i] = countDic.get(i,0) + 1

for num, count in countDic.items():
    print(num, count)
