# 크게 만들기 (2812)
## 난이도 : 골드 3

import sys

num_cnt, out_cnt = list(map(int, input().split()))
nums = input()
result = []
result.append(nums[0])
idx = 1

while out_cnt != 0:
    temp_num = nums[idx]
    if temp_num <= result[-1]:
        result.append(temp_num)
    else:
        size = len(result)
        for i in range(size):
            if out_cnt ==0 :
                break
            if temp_num <= result[-1]:
                break
            else:
                result.pop()
                out_cnt -= 1
        result.append(temp_num)
    idx += 1

if idx < num_cnt-1:
    for i in range(idx, num_cnt):
        result.append(nums[i])

print(''.join(result))