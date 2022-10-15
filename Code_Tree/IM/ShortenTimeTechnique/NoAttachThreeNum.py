# 인접하지 않은 3개의 숫자
## n개의 숫자가 주어졌을 때, 서로 인접하지 않도록 3개의 숫자를 적절하게 골라 합이 최대가 되도록 하는 프로그램을 작성해보세요.
### 테크닉 : LR 테크닉

size = int(input())

numList = list(map(int, input().split()))

L = [0 for i in range(size)]
R = [0 for i in range(size)]
bigL = 0
bigR = 0
for i in range(size):
    tempL = numList[i]
    tempR = numList[size-i-1]
    bigL = max(tempL,bigL)
    bigR = max(tempR,bigR)
    L[i] = bigL
    R[size-i-1] = bigR


big = 0
for i in range(size):
    left = i - 1
    right = i + 1
    if left > 0 and right < size-1:
        temp = numList[i] + L[left-1] + R[right+1]
        big = max(temp,big)
print(big)