# 연속 부분 합의 최댓값 구하기

size = int(input())
nums = list(map(int,input().split()))

result = [0 for _ in range(size)]
result[0] = nums[0]

for idx in range(1,size):
    result[idx] = max(nums[idx],result[idx-1] + nums[idx])

print(max(result))