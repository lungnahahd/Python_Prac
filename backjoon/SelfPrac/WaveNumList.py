# 파도반 수열 (9461)
## 난이도 : 실버 3

import sys
input = sys.stdin.readline 

case_num = int(input())

wave = [1,1,1,2,2]
for idx in range(5,100):
    now_val = wave[idx-5] + wave[idx-1]
    wave.append(now_val) 

for _ in range(case_num):
    now_point = int(input())
    print(wave[now_point-1])
