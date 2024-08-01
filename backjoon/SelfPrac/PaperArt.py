# 종이접기 (1892)
## 난이도 : 실버 1


case_count = int(input())
state_list = []
for _ in range(case_count):
    now = list(input())
    state_list.append(now)

now_idx = 0
while now_idx < case_count:
    now_state = state_list[now_idx]
    now_size = len(now_state)
    mid_idx = now_size // 2
    left_idx, right_idx = mid_idx - 1, mid_idx + 1
    nowResult = "YES"
    while left_idx >= 0:
        if (now_state[left_idx] == now_state[right_idx]):
            nowResult = "NO"
            break
        left_idx, right_idx = left_idx - 1, right_idx + 1
    print(nowResult)
    now_idx += 1