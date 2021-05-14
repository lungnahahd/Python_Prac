# 알파벳과 숫자가 문자열로 주어지면 모든 알파벳은 오름차순으로 정렬, 숫자는 더해서 맨 뒤에 출력

import sys
input = sys.stdin.readline

give_string = input().strip()
count = 0

sort = sorted(give_string, reverse=False)
sort = ''.join(sort)

for i in range(len(sort)):
    if sort[i].isdigit():
        count  += int(sort[i])
    else:
        result = sort[i:]
        break
result = result + str(count)
print(result)