# 차이를 최대로 (10819)
## 난이도 : 실버 2

import sys 
input = sys.stdin.readline 

temp_num = []
temp = set()
answer = 0
cnt = int(input())
num_list = list(map(int, input().split()))

def cal_num(n_lst):
    val = 0
    for idx in range(cnt-1):
        val += abs(n_lst[idx] - n_lst[idx+1])
    
    return val


def back_track():
    global temp_num, answer

    if len(temp_num) == cnt:
        answer = max(answer, cal_num(temp_num))
    
    for idx in range(cnt):
        if idx not in temp:
            temp.add(idx)
            temp_num.append(num_list[idx])
            back_track()
            temp_num.pop()
            temp.remove(idx)


back_track()
print(answer)