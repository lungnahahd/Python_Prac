# 등수 매기기 (2012)
## 난이도 : 하

import sys

input = sys.stdin.readline

cnt = int(input())

chk_num = [False for _ in range(500001)] # 수를 확인하기 위한 배열

remain_num = []
rst = 0

for _ in range(cnt):
    temp = int(input()) 
    if chk_num[temp] or temp > cnt: # 해당 등수가 이미 존재하거나, 예상 등수가 사람 수보다 많을 때 남은 수로 추가
        remain_num.append(temp)
    else:
        chk_num[temp] = True

remain_num.sort(reverse=True)

# 남은 수를 이용해서 차이를 계산
for idx in range(1, cnt+1):
    if chk_num[idx]:
        continue
    now_remain = remain_num.pop()
    rst += abs(now_remain - idx)
print(rst)