# 가잗 큰 증가 부분 수열
## 수열이 주어졌을때, 증가 부분 수열 중 합이 가장 큰 것을 구하기
### 입력 : 첫 줄에 수열의 크기가 입력되고, 둘째 줄에 수열이 직접 입력
### 출력 : 수열의 합이 가장 큰 증가 부분 수열의 합을 출력
import sys

input = sys.stdin.readline

size = int(input()) # 수열의 크기
list = input().split() # 수열 입력

count = [[] for i in range(size)]

for i in range(size):
    count[i].append(int(list[i]))
    count[i].append(int(list[i]))
    count[i].append(int(list[i]))

result = [] # 각 시작 경우의 최대를 담을 배열
for a in range(size):
    for b in range(a+1,size):
        for c in range(b,size):
            if int(list[c]) > count[a][2]:
                count[a][1] += int(list[c])
                count[a][2] = int(list[c])
        count[a][0] = max(count[a][0],count[a][1])
        count[a][1] = int(list[a])
        count[a][2] = int(list[a])
    result.append(count[a][0])

print(max(result))

     