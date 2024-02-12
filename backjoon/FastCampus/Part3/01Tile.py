# 01 타일( 1904 )
## 난이도 : 하

import sys 
input = sys.stdin.readline

tiles = [1, 2]
before = 1

target = int(input())

def TileCheck(num)


if target < 3:
    print(tiles[target-1])
else:
    for idx in (2,target-1):
        tiles.append((tiles[idx-2] * 2 + 1) % 15746)
    print(tiles[-1])