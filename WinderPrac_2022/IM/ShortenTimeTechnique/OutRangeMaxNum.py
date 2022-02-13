# 구간 외 최대 숫자
## n개의 숫자가 주어졌을 때, q개의 질의에 대해 주어진 구간 밖에 있는 숫자들 중 최댓값을 출력하는 프로그램을 작성해보세요.
## 단, 구간은 n개의 숫자의 번호에 해당하는 숫자로 주어집니다.

numSize, cmdSize = input().split()
numSize = int(numSize)
cmdSize = int(cmdSize)

numS = list(map(int, input().split()))

L = [0 for i in range(numSize + 1)]
R = [0 for i in range(numSize + 1)]

bigL = 0
bigR = 0
for i in range(numSize):
    tempL = numS[i]
    tempR = numS[numSize - i - 1]
    bigL = max(tempL,bigL)
    L[i + 1] = bigL
    bigR = max(tempR, bigR)
    R[numSize - i - 1] = bigR


for i in range(cmdSize):
    front, back = input().split()
    front, back = int(front), int(back)
    result = max(L[front-1],R[back])
    print(result)
