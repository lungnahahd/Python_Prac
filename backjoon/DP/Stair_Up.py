# 계단 오르기

size = int(input())

stairs = []

for _ in range(size):
    s = int(input())
    stairs.append(s)

mid_result = [0 for _ in range(6)]

for step_size in stairs:
    temp_3, temp_4, temp_5 = mid_result[0], mid_result[1], mid_result[2]
    mid_result[3], mid_result[4], mid_result[5] = temp_3, temp_4, temp_5
    mid_result[0] = max(temp_4, temp_5)
    mid_result[1] = step_size + temp_3
    mid_result[2] = step_size + temp_4

print(max(mid_result[0], mid_result[1], mid_result[2]))




## 반례
# 10
# 3
# 5
# 10 
# 9
# 2
# 1
# 2
# 5
# 2
# 9
# 38
