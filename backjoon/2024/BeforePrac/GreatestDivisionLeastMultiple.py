# 최대공약수, 최소공배수 구하기
## 두 개의 자연수를 입력 받아서 최대 공약수와 최소 공배수를 출력하는 프로그램
### 입력 : 첫째 줄에는 두 개의 자연수 제공
### 출력 : 첫째 줄에는 최대공약수, 둘째 줄에는 최소공배수 출력

import sys
sys.stdin.readline
# 입력 받은 두 수를 큰 것과 작은 것으로 구분하기
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

GD = False # 최대공약수 찾기 성공 여부를 알려주는 변수
GDNum = 0 # 최대공약수를 담는 변수
check = small # 최대공약수를 찾는 기준이 되는 변수 -> 해당 변수를 바꾸어가면서 최대공약수를 찾아나갈 것
# 최대공약수를 구하는 부분
while not GD:
    if small % check == 0: 
        if big % check == 0:
            GD = True # 최대공약수를 찾으면 반복문 종료
            GDNum = check # 찾은 최대공약수를 담기
        else:
            check -= 1 # 해당 수가 최대공약수가 아니라면 행하는 부분
    else:
        check -= 1 # 해당 수가 최대공약수가 아니라면 행하는 부분
    if check == 0: # 끝까지 찾아는데 없으면 그냥 반복문 탈출
        break

LM = False # 최소공배수 찾기 성공 여부를 알려주는 변수
LMNum = 0 # 최소공배수를 담는 변수
check = 1 # 최소공배수를 찾기 위해 곱하기를 해주는 변수 -> 점점 증가시켜서 최소공배수를 찾아나가기
# 최소공배수를 구하는 부분
while not LM:  
    increaseNum = big * check # 최소공배수를 찾는 실질적 변수
    if increaseNum % small == 0:
        LM = True # 최소공배수를 찾았을 경우 반복문 탈출
        LMNum = increaseNum # 최소공배수를 담는 변수
    else:
        check += 1 # 최소공배수가 아닐 경우 점점 수를 늘려가면서 최소공배수 찾기
# 결과를 출력
print(GDNum)
print(LMNum)