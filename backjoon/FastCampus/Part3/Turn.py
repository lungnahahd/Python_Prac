# 뒤집기 (1439)
## 난이도 : 하


num_list = list(input())

one_cnt, zero_cnt = 0, 0

before = num_list[0]

for num in num_list:
    if before != num:
        if before == '0':
            zero_cnt += 1
        else:
            one_cnt += 1
        before = num
if before == '0':
    zero_cnt += 1
else:
    one_cnt += 1
    
rst = min(one_cnt, zero_cnt)
if rst == 0 and one_cnt != zero_cnt:
    rst = max(one_cnt, zero_cnt)

print(rst)