# 코딩은 예쁘게 (2879)
## 난이도 : 골드 3

import sys
input = sys.stdin.readline 

count_line = int(input())

origin_line = list(map(int, input().split()))
line_format = list(map(int, input().split()))
different_list = []

for idx in range(count_line):
    different_list.append(origin_line[idx]-line_format[idx])

result = 0

while True:
    check = set(different_list)
    if len(check) == 1 and different_list[0] == 0:
        break

    remove_value = abs(different_list[0])
    save_idx = [0]
    finished = False
    for now in range(1, count_line):
        if different_list[now-1] == 0:
            remove_value = abs(different_list[now])
            save_idx.append(now)
            finished = False
        elif different_list[now-1] * different_list[now] > 0:
            save_idx.append(now)
            remove_value = min(remove_value, abs(different_list[now]))
            finished = False
        else:
            if different_list[now] == 0:
                finished = True
            else:
                finished = False
            while save_idx:
                out_idx = save_idx.pop()
                if different_list[out_idx] < 0:
                    different_list[out_idx] += remove_value
                elif different_list[out_idx] > 0:
                    different_list[out_idx] -= remove_value
            result += remove_value
            save_idx.append(now)
            remove_value = abs(different_list[now])
    
    if not finished:
        while save_idx:
            out_idx = save_idx.pop()
            if different_list[out_idx] < 0:
                different_list[out_idx] += remove_value
            elif different_list[out_idx] > 0:
                different_list[out_idx] -= remove_value
        result += remove_value
    #break

print(result)