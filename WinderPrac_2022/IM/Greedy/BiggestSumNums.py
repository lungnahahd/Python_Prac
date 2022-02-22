# 연속 부분 합의 최대값 구하기
## n개의 정수가 입력으로 주어지고, 이 중 연속한 부분 수열에 속한 원소들의 합이 최대가 될 때의 값을 출력하는 코드를 작성해보세요. (단, 부분 수열은 최소 한 개 이상의 원소를 포함합니다.)
### 테크닉 : 그리디 알고리즘

import sys
INT_MAX = sys.maxsize

count = int(input())
numS = list(map(int, input().split()))

sumNum = -INT_MAX # 연속되는 수를 계속 갱신해주는 변수
result = -INT_MAX # 가장 최대의 값을 갱신해주는 변수
for i in numS:
    if i >= 0: # 양수인 경우는 계쏙 더해가기
        if sumNum < 0:
            sumNum = i
        else:    
            sumNum += i
        result = max(result,sumNum)
    else:
        sumNum += i
        if sumNum < 0:
            result = max(result,i)
            result = max(result, sumNum)
        else:
            result = max(result,sumNum)
print(result)

#### 모범코드
# import sys

# INT_MIN = -sys.maxsize

# # 변수 선언 및 입력
# n = int(input())
# arr = [0] + list(map(int, input().split()))

# # 최댓값을 구해야 하는 문제이므로
# # 초기값을 INT_MIN으로 설정합니다.
# ans = INT_MIN

# # 현재 연속 부분 수열 내 원소의 합을
# # 저장합니다.
# sum_of_nums = 0;

# for i in range(1, n + 1):
#     # 만약 현재 연속 부분 수열 내 원소의 합이
#     # 0보다 작아진다면, 지금부터 새로운
#     # 연속 부분 수열을 만드는 것이 더 유리합니다.
#     if sum_of_nums < 0:
#         sum_of_nums = arr[i]
    
#     # 그렇지 않다면 기존 연속 부분 수열에 
#     # 현재 원소를 추가하는 것이 더 좋습니다.
#     else:
#         sum_of_nums += arr[i]
    
#     ans = max(ans, sum_of_nums)

# print(ans)