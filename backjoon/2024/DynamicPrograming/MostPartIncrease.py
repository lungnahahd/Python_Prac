# 가장 큰 증가 부분 수열
## 수열이 주어졌을때, 증가 부분 수열 중 합이 가장 큰 것을 구하기
### 입력 : 첫 줄에 수열의 크기가 입력되고, 둘째 줄에 수열이 직접 입력
### 출력 : 수열의 합이 가장 큰 증가 부분 수열의 합을 출력
import sys

input = sys.stdin.readline

size = int(input()) # 수열의 크기
list = input().split() # 수열 입력

result = [0 for i in range(size)] #  각 경우에서 최대를 나타낼 값을 나타내주는 배열
result[0] = int(list[0])

# 점점 배열 확인 범위를 늘려나가면서 각 경우일 때, 최대의 값을 result에 저장하기!
# 한 번 변경된 result의 값은 변하지 않음으로 이를 이용해서 다이나믹 알고리즘 적용
for i in range(1,size):
    temp = 0
    for j in range(i):
        if int(list[j]) < int(list[i]):
            if temp < result[j]:
                temp = result[j]
    result[i] = temp + int(list[i])

print(max(result))