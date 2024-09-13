# 퇴직2 (15486)
## 난이도 : 골드 5

import sys
input = sys.stdin.readline 

day_num = int(input())
time_table, money_table= [0], [0]
stack_money = [0 for _ in range(day_num+1)]

for _ in range(day_num):
    time, money = list(map(int, input().split()))
    time_table.append(time)
    money_table.append(money)


for idx in range(1, day_num+1):
    if (time_table[idx] + idx -1) > day_num:
        continue
    #stack_money[time_table[idx]+idx-1] = max(stack_money[time_table[idx]+idx-1], stack_money[idx-1] + money_table[idx])
    stack_money[time_table[idx]+idx-1] = max(max(stack_money[:idx]) + money_table[idx], max(stack_money[:time_table[idx]+idx]))
#print(stack_money)
print(max(stack_money))