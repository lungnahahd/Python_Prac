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

# 파이썬은 1초에 어림잡아 2000만번 연산을 수행 가능
# 여기서 전체 경우의 수는 24*60*60=86400번 이므로 충분히 하나씩 연산해도 시간 문제 X
# 참고 답안
# h = int(input())
# count = 0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             #시분초를 나열해서 문자열로 만들고 거기서 3이 포함되어 있으면 카운트 증가
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
# print(count)
    