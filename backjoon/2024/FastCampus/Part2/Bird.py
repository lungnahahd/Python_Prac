# 새 (1568)
## 난이도 : 하

import sys

cnt_bird = int(input())
sing = 1
second = 0

while cnt_bird > 0:
    if (sing > cnt_bird): # 새의 수가 지금 불러야 하는 수보다 작은 경우
        sing = 1
        continue
    cnt_bird -= sing
    second += 1
    sing += 1

print(second)