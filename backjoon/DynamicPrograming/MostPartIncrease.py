# 가장 큰 증가 부분 수열
## 수열이 주어졌을때, 증가 부분 수열 중 합이 가장 큰 것을 구하기
### 입력 : 첫 줄에 수열의 크기가 입력되고, 둘째 줄에 수열이 직접 입력
### 출력 : 수열의 합이 가장 큰 증가 부분 수열의 합을 출력
import sys

input = sys.stdin.readline

size = int(input()) # 수열의 크기
list = input().split() # 수열 입력

count = [[] for i in range(size)]

# count의 0 인덱스는 해당 위치 값을 포함, 1 인덱스는 해당 위치 값을 포함 X
count[0].append([int(list[0]),int(list[0])])
count[0].append([0,0])
print(count)
for i in range(1,size):
    













# for i in range(size):
#     count[i].append(int(list[i]))
#     count[i].append(int(list[i]))
#     count[i].append(int(list[i]))

# result = [] # 각 시작 경우의 최대를 담을 배열
# min = 1001
# for a in range(size):
#     if min > int(list[a]):
#         min = int(list[a])        
#         b = a+1
#         c = b
#         while c < size:
#             if int(list[c]) > count[a][2]:
#                 count[a][1] += int(list[c])
#                 count[a][2] = int(list[c])
#             c += 1
#             if c == size:
#                 b += 1
#                 c  = b
#                 count[a][0] = max(count[a][0],count[a][1])
#                 count[a][1] = int(list[a])
#                 count[a][2] = int(list[a])
#             if b == size:
#                 break
#         result.append(count[a][0])
# print(max(result))
# print(result)

# 해당 반례 해결하기(228 - 10)
# 2 11 3 14 1 200 100 5 101 13
# 해당 반례 해결하기(363 - 15)
# 115 5 82 81 63 130 80 93 122 81 58 25 63 66 22

     