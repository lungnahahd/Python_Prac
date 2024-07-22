# 코딩은 예쁘게 (2879)
## 난이도 : 골드 3

import sys
input = sys.stdin.readline 

count_line = int(input())

origin_line = list(map(int, input().split()))
line_format = list(map(int, input().split()))

result = 0

different_value = origin_line[0] - line_format[0]
temp_point = abs(different_value)
finish = False
for idx in range(1, count_line):
    if different_value * (origin_line[idx] - line_format[idx]) < 0:
        result += temp_point
        different_value = origin_line[idx] - line_format[idx]
        temp_point = abs(different_value)
        finish = True
    elif different_value * (origin_line[idx] - line_format[idx]) > 0:
        different_value = origin_line[idx] - line_format[idx]
        temp_point = max(temp_point, abs(different_value))
        finish = False
    else:
        if different_value == 0:
            different_value = origin_line[idx] - line_format[idx]
            temp_point = abs(different_value)
            finish = False
        else:
            result += temp_point
            different_value = 0
            temp_point = 0
            finish = True
if not finish:
    result += temp_point
print(result)
