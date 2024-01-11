# 사이클게임
## 난이도 : 중

import sys
input = sys.stdin.readline

point_num, stage_num = list(map(int, input().split()))

paraents = [idx for idx in range(point_num)]

def find_mother(node):
    if node == paraents[node]:
        return paraents[node]
    else:
        return find_mother(paraents[node])

def union(x, y):
    x_mother = find_mother(x)
    y_mother = find_mother(y)
    if(x_mother <= y_mother):
        paraents[y] = x_mother
    else:
        paraents[x] = y_mother

def chk_cycle(paraents, x, y):
    if (paraents[x] == paraents[y]):
        return True
    else:
        return False

not_fin = True
rst_stage = 0

for stage in range(1,stage_num+1):
    x, y = list(map(int, input().split()))
    if(not_fin and chk_cycle(paraents, x, y)):
        not_fin = False
        rst_stage = stage
    union(x,y)

print(rst_stage)