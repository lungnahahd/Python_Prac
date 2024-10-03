# 행복한 수열의 개수


import sys
input = sys.stdin.readline

size, check = list(map(int, input().split()))

place = []
for _ in range(size):
    temp = list(map(int, input().split()))
    place.append(temp)
import sys
input = sys.stdin.readline

size, check = list(map(int, input().split()))

place = []
for _ in range(size):
    temp = list(map(int, input().split()))
    place.append(temp)

answer = 0

if size == 1 and check == 1:
    answer = 2


# 동일 행 내부 판단
for r in range(size):
    cnt = 1
    already_count = False
    for c in range(size-1):
        if place[r][c] == place[r][c+1]:
            cnt += 1
        else:
            cnt = 1
        if cnt == check:
            answer += 1
            break

# 동일 열 내부 판단
for c in range(size):
    cnt = 1
    for r in range(size-1):
        if place[r][c] == place[r+1][c]:
            cnt += 1
        else:
            cnt = 1

        if cnt == check:
            answer += 1
            break

print(answer)