# 문제
# 어떤 수 getnum이 1이 될때까지 다음의 두 과정은 반복적으로 수행, 단 2번째 연산은 getnum이 divisionnum으로 나누어 질 경우만 선택 가능
#     1. getnum에서 1을 빼는 연산
#     2. getnum을 divisionnum으로 나누는 연산
# getnum과 divisionnum이 주어질 때, 1이 될 때까지의 최소 연산을 출력하는 프로그램을 작성하시오



import sys
input = sys.stdin.readline

# 아래의 코드를 한줄로 정리 가능
# -> 띄어쓰기를 기준으로 두 수를 나누고 이를 int형으로 변환하라는 코드 의미
# getnum, divisionnum = map(int, input().split())
getnum = input().strip()
divisionnum = input().strip()
getnum = int(getnum)
divisionnum = int(divisionnum)
count = 0

while getnum != 1:
    if getnum % divisionnum == 0:
        getnum = getnum / divisionnum
    else:
        getnum = getnum - 1
    count += 1
print(count)

# 시간 복잡도를 줄일 수 있는 코드
# 아래 코드를 활용해서 시간 복잡도를 기하급수적으로 줄일 수 있다.
# while True:
#     #getnum이 divisionnum으로 나누어 떨어지는 가장 큰 수를 구함
#     target = (getnum // divisionnum) * divisionnum
#     # getnum이 target(divisionnum)으로 될 때까지 1을 빼는 연산을 몇 번 수행할지 계산해서 이를 한 번에 넣어주는 과정
#     count += (getnum - target)
#     getnum = target
#     # getnum < target이 되면 더 이상 나누기 연산을 할 수 없으므로 반복문 나오기
#     if getnum < divisionnum:
#         break
#     # 나누기 연산이 가능하다면 한 번 나누어주고 다시 while문 돌기
#     count += 1
#     getnum //= divisionnum
# # 나눌 수 없고 빼기 연산만 가능한 경우 -1씩 빼주는 연산을 한 번에 수행하기 
# count += (getnum - 1)
# print(count)