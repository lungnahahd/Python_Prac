# 가장 긴 바이토닉 부분 수열
## 수열이 입력되었을 때, 가장 긴 바이토닉 부분 수열의 길이를 출력
### 입력 : 첫 줄의 수열의 길이와 두번 째 줄에 수열을 입력
### 출력 : 주어진 수열의 가장 긴 바이토닉 부분 수열의 길이를 출력

from gettext import install
import sys
input = sys.stdin.readline

size = int(input())
list = input().split()
reverseList = list
reverseList.reverse()

increase = [1 for i in range(size)]
reIncrease = [1 for i in range(size)]

result = [0 for i in range(size)]

# 각 위치에서 증가하는 배열의 길이 구하기
for i in range(1,size):
    big = 0
    reverse = 0
    for j in range(i):
        if int(list[i]) > int(list[j]):
            if big < increase[j]:
                big = increase[j]
        if int(reverseList[i]) > int(reverseList[j]):
            if reverse < reIncrease[j]:
                reverse = reIncrease[j]
    increase[i] += big
    reIncrease[i] += reverse
reIncrease.reverse()

print(reIncrease[8:])
print(increase[:7])

for i in range(size):
    if i != 0 and i != size-1:
        front = increase[:i]
        back = reIncrease[i+1:]
        big = 0
        small = 0
        for j in range(i):
            if int(list[i]) > int(list[j]):
                if big < front[j]:
                    big = front[j]
        for k in range(len(back)):
            if int(list[i]) > int(list[k+i+1]):
                if small < back[k]:
                    small = back[k]
        print(big)
        print(small)
        result[i] = big + small + 1

# for i in range(1,size):
#     if int(list[0]) > int(list[i]):
#         if result[0] < increase[i]:
#             result[0] = increase[i] + 1


# for i in range(size-1):
#     big =0
#     if int(list[size-1]) > int(list[i]):
#         if result[size-1] < reIncrease[i]:
#             result[size-1] = reIncrease[i] + 1



# print(increase)
# print(reIncrease)
# print(result)
