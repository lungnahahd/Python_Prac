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