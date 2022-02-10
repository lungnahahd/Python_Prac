# 서로 다른 숫자
## n개의 숫자가 주어졌을 때, 서로 다른 숫자의 수를 출력하는 프로그램을 작성해보세요.
### Set 사용 이유 : 중복을 허용하지 않고, 순서를 지킬 필요가 없기 때문에 사용

size = int(input())

eleNum = list(map(int,input().split()))
eleSet = set()

for i in eleNum:
    eleSet.add(i)

print(len(eleSet))