# Python 활용 버블 정렬 구현 
# 바로 옆의 원소와의 크기를 비교하여 작은 수를 왼쪽으로 이동하는 과정을 더 이상 정렬할 경우가 없을 떄까지 진행!! 


n = int(input())
nums = list(map(int, input().split()))
sortAble = True

while(sortAble):
    sortAble = False
    for i in range(n-1):
        if (nums[i] > nums[i+1]):
            sortAble = True
            nums[i], nums[i+1] = nums[i+1], nums[i]

for num in nums:
    print(num, end= ' ')
