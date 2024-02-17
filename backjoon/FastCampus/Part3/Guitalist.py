# 기타리스트 (1495)
## 난이도 : 중

import sys 

input = sys.stdin.readline

cnt_song, start, max_volumn = list(map(int, input().split()))

dp_volumn = [[False for _ in range(max_volumn+1)] for _ in range(cnt_song+1)] # 다이나믹 배열
dp_volumn[0][start] = True
list_volumn = list(map(int, input().split())) # 볼륨 차이 리스트

# 다이나믹 배열을 갱신하는 부분 
for song in range(1,cnt_song+1):
    for volumn in range(max_volumn+1):
        if dp_volumn[song-1][volumn]:
            if(volumn - list_volumn[song-1] >= 0):
                dp_volumn[song][volumn - list_volumn[song-1]] = True
            if(volumn + list_volumn[song-1] <= max_volumn):
                dp_volumn[song][volumn + list_volumn[song-1]] = True

result = -1

for idx in range(max_volumn, -1, -1):
    if dp_volumn[-1][idx]:
        result = idx
        break

print(result)