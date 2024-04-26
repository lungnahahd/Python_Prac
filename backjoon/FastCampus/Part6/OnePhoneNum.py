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
        phones.append(int(input()))
    temp_save = set()
    len_save = []
    phones.sort()
    temp_save.add(phones[0])
    len_save.append(len(str(phones[0])))

    for phone in phones[1:]:
        if finish:
            break
        for len_val in len_save:
            temp = str(phone)[:len_val]
            if int(temp) in temp_save:
                finish = True
                result.append("NO")
                break
        temp_save.add(phone)
        len_save.append(len(str(phone)))
    if not finish:
        result.append("YES")
    
for rst in result:
    print(rst)