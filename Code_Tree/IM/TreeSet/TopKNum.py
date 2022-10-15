# top K 숫자
## n개의 숫자가 주어졌을 때, 중복을 제외하고 내림차순으로 정렬했을 때 앞에 있는 k개의 숫자를 출력하는 프로그램을 작성해보세요.
### TreeSet 사용 이유 : 중복을 허용하지 않고, 내림차순 정렬이 필요하므로 사용

from sortedcontainers import SortedSet

s = SortedSet()      # treeset

numSize = list(map(int,input().split()))
numList = list(map(int,input().split()))

numSet = SortedSet(numList)


for i in range(numSize[1]):
    where = i + 1
    print(numSet[-where],end=' ')