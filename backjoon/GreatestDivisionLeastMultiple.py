# 최대공약수, 최소공배수 구하기
## 두 개의 자연수를 입력 받아서 최대 공약수와 최소 공배수를 출력하는 프로그램
### 입력 : 첫째 줄에는 두 개의 자연수 제공
### 출력 : 첫째 줄에는 최대공약수, 둘째 줄에는 최소공배수 출력

import sys
sys.stdin.readline

big = 0
small = 0

a , b = input().split()
a = int(a)
b = int(b)

if a > b:
    big = a
    small = b
else:
    big = b
    small = a

GD = False
GDNum = 0
check = small

while not GD:
    if small % check == 0:
        if big % check == 0:
            GD = True
            GDNum = check
        else:
            check -= 1
    else:
        check -= 1
    if check == 0:
        break

LM = False
LMNum = 0
check = 1

while not LM:
    big = big * check
    if big % small == 0:
        LM = True
        LMNum = big
    else:
        check += 1

print(GDNum)
print(LMNum)