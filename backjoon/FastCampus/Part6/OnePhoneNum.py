# 전화번호 목록 (5052)
## 난이도 : 골드 4

import sys
input = sys.stdin.readline 

case_cnt = int(input())

result = []
for _ in range(case_cnt):
    phone_cnt = int(input())
    finish = False
    phones = []
    for _ in range(phone_cnt):
        temp = input()
        phones.append(temp[:len(temp)-1])
    phones.sort()
    for idx in range(len(phones)-1):
        if phones[idx] == phones[idx+1][:len(phones[idx])]:
            finish = True
            result.append("NO")
            break
    if not finish:
        result.append("YES")

for rst in result:
    print(rst)