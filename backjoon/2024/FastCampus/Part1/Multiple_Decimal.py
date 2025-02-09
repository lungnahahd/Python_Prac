# 소수의 곱 (2014)
## 난이도 : 

import sys

input = sys.stdin.readline

cnt_num, want = list(map(int, input().split()))
num_list = list(map(int, input().split()))

chk_num = [False for _ in range(want * 2**want + 1)]

for num in num_list:
    for multi in range(1, want+1):
        idx = num**multi
        if (idx <= len(chk_num)):
            chk_num[idx] = True 

temp_rst = 0
idx = 2
result = 0
while temp_rst != want:
    if (chk_num[idx] == True):
        temp_rst += 1
        result = idx
        for num in num_list:
            if(num*idx <= len(chk_num)):
                chk_num[num*idx] = True
    idx += 1

print(result)