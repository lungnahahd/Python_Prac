# 대칭 차집합
## 대칭 차집합이란, 두 집합 A와 B가 있을때 집합 A - B 와 집합 B - A 의 합집합을 대칭 차집합 이라고 한다.
## 자연수를 원소로 갖는 두 집합 A와 B에 대한 대칭 차집합의 원소의 개수를 구하는 프로그램을 작성하세요.
### Set 이용 이유 : 단순 값의 유무만 판단하면 되므로 빠르게 이를 파악하기 위해서 사용

numSize = list(map(int,input().split()))

numA = list(map(int,input().split()))
setA = set(numA)
numB = list(map(int,input().split()))
setB = set(numB)

for i in numA:
    if i in setB:
        setB.remove(i)

for i in numB:
    if i in setA:
        setA.remove(i)
print(len(setA)+ len(setB))