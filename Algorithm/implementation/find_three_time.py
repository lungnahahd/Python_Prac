# 정수 N이 입력되면 **시 **분 &&초 부터 모든 시각 중에서 3이 포함되는 경우를 count하기
# 첫째 줄에 정수 N을 입력하기

import sys
input = sys.stdin.readline

hour = input().strip()
hour = int(hour)
count = 0

case1 = 60 * 60
case2 = 15 * 60 + 45 * 15

for i in range(hour + 1):
    if i == 3:
        count = count + case1
    elif i == 23:
        count = count + case1
    else:
        count = count + case2
print(count)
    