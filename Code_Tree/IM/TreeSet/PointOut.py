# 점 뺴기
## 2차 평면 위에 서로 다른 n개의 점이 주어집니다. 이후 m개의 질의가 주어지는데, 각 질의마다는 한 개의 숫자 k가 주어집니다. 각 질의에 대해 주어진 숫자 k보다 x값이 같거나 큰 점 중 x값이 가장 작은 점을 찾아 지우려고 합니다. 
## 만약 x값이 가장 작은 점이 여러 개라면, 그 중 y값이 가장 작은 점을 지우면 됩니다. 각 질의에 대해 해당하는 점을 순서대로 출력하고 지우는 프로그램을 작성해보세요.
### TreeSet 사용 이유 : 큰 것중에 작은 것을 빼고, y 값 역시 동시에 비교해주기 위해 사용



from sortedcontainers import SortedSet

s = SortedSet()

cmd = list(map(int, input().split()))
for i in range(cmd[0]):
    x, y = input().split()
    s.add((int(x),int(y)))

for i in range(cmd[1]):
    numX = int(input())
    where = s.bisect_left((numX,0))
    if where >= len(s):
        print(-1, -1)
    else:
        x, y = s[where]
        print(x, y)
        s.remove(s[where])