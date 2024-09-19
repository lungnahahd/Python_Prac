# 좀비 떼가 기관총 진지에도 오다니 (19644)
## 난이도 : 골드 3

import sys
input = sys.stdin.readline

zombie_cnt = int(input())
gun_dist, gun_power = list(map(int, input().split()))
bomb_cnt = int(input())

zombies = [0 for _ in range(zombie_cnt)]
for idx in range(zombie_cnt):
    zombies[idx] = int(input())

die = False

for target in range(zombie_cnt):
    if zombies[target] - gun_power > 0:
        if bomb_cnt > 0:
            bomb_cnt -= 1
            continue
        else:
            die = True
            break
    for idx in range(gun_dist):
        if target + idx >= zombie_cnt:
            break
        zombies[target + idx] -= gun_power

if die:
    print("NO")
else:
    print("YES")