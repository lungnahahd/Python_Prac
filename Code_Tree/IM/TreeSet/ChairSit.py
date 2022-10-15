# 자리 찾기

### TreeSet 사용 이유 : 의자 위치는 정렬이 필요하고, 계속 조회를 해야하므로 사용

from sortedcontainers import SortedSet

s = SortedSet()      # treeset

cmd = list(map(int,input().split()))
peopleWant = list(map(int, input().split()))
peopleWant.sort(reverse=True)

chairSet = SortedSet()
chair = []
for i in range(cmd[1]):
    chairSet.add(i+1)

resultCount = 0




for i in peopleWant:
    idx = chairSet.bisect_right(i)-1
    if i in chairSet:
        chairSet.remove(i)
        resultCount += 1
    else:
        if idx < 0:
            #print(i)
            break
        else:
            chairSet.remove(chairSet[idx])
            resultCount += 1
            
print(resultCount)