# 성 지키기 (1236)
## 난이도 : 하

row, col = list(map(int, input().split()))

castle = []

for _ in range(row):
    temp = input()
    castle.append(temp)

row_result = 0

for row_idx in range(row):
    not_have = True
    for col_idx in range(col):
        if castle[row_idx][col_idx] == "X":
            not_have = False
            break
    if not_have:
        row_result += 1

col_result = 0 

for col_idx in range(col):
    not_have = True
    for row_idx in range(row):
        if castle[row_idx][col_idx] == "X":
            not_have = False
            break
    if not_have:
        col_result += 1

if (row_result >= col_result):
    print(row_result)
else:
    print(col_result)