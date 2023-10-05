## 주어진 그리드에서 3x3 도장(?)을 찍어 최대의 값이 나올 수 있도록 설정
## 간단하게 합을 미리 구해서 이를 이용해서 최대 값을 구할 수 있도록 구현


size = int(input())
numSum = [[0 for _ in range(size-2)] for _ in range(size)]

# 입력을 받으면서 가로로 3개씩 더했을 떄의 값만을 리스트로 저장
for i in range(size):
    nums = list(map(int, input().split()))
    for idx in range(2,len(nums)):
        numSum[i][idx-2] = nums[idx] + nums[idx-1] + nums[idx-2]

result = -1
# 세로로 반복하여 처리
for i in range(0,size-2):
    for k in range(2,size):
        result = max(result, numSum[k][i]+numSum[k-1][i] + numSum[k-2][i])
       
print(result)
