# 종이접기 (1892)
## 난이도 : 실버 1


case_count = int(input())
state_list = []
for _ in range(case_count):
    now = list(input())
    state_list.append(now)

def check(now_list):
    now_size = len(now_list)
    mid_idx = now_size // 2

    left_idx, right_idx = mid_idx - 1, mid_idx + 1
    nowResult = 1
    while left_idx >= 0:
        if (now_list[left_idx] == now_list[right_idx]):
            nowResult = 0
            break
        left_idx, right_idx = left_idx - 1, right_idx + 1
    return nowResult

answer = 1
def main_work(now_list):
    global answer
    answer = min(answer, check(now_list))
    new_left_end = len(now_list) // 2 - 1
    if new_left_end < 0:
        return
    else:
        new_rieght_start = len(now_list) // 2 + 1
        main_work(now_list[0:new_left_end+1])
        main_work(now_list[new_rieght_start: len(now_list)])



now_idx = 0
while now_idx < case_count:
    answer = 1
    main_work(state_list[now_idx])
    if answer == 1:
        print("YES")
    else:
        print("NO")
    now_idx += 1

