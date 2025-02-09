# 가장 높은 탑 쌓기 (2655)
## 난이도 : 상

import sys
import copy

input = sys.stdin.readline

cnt_block = int(input())

max_high = 0
save_block = [[[] for _ in range(100*10000 + 1)] for _ in range(cnt_block)]
origin_block = []
for idx in range(1, cnt_block + 1):
    size, height, weight = list(map(int, input().split()))
    max_high += height
    save_block[0][height].append(([idx], size, weight))
    origin_block.append((size, weight, height, idx))

rst_use_block = 0
rst_high = 0
for use_block in range(1, cnt_block):
    end_chk = True
    for high in range(1, max_high+1):
        if len(save_block[use_block-1][high]) == 0:
            continue
        for now in range(len(save_block[use_block-1][high])):
            now_idx, now_size, now_weight = save_block[use_block-1][high][now]
            for idx in range(cnt_block):
                origin_size, origin_weight, origin_height, origin_idx = origin_block[idx]
                if origin_size >= now_size or origin_weight >= now_weight:
                    continue
                temp_idx = copy.deepcopy(now_idx)
                now_high = high + origin_height
                temp_idx.append(origin_idx)
                save_block[use_block][now_high].append((temp_idx, origin_size, origin_weight))
                rst_high = max(rst_high, now_high)
                end_chk = False
    if end_chk:
        rst_use_block = use_block
        break

print(rst_use_block)
rst_idx, _, _ = save_block[rst_use_block-1][rst_high][0]
for rst in rst_idx:
    print(rst)