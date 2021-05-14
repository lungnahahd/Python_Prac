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
if count == 0:
    result = result
else:
    sresult = result + str(count)
print(result)

# 참고 답안
# 문자열을 그냥 별도에 리스트에 저장하고 숫자는 내가 하던대로 계산 진행
# 마지막 출력에 리스트를 정렬하고 숫자의 합을 마지막에 붙이면 정답 가능
data = input()
result = []
value = 0
# 문자를 하나식 확인
for x in data:
    #알파벳인 경우는 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자인 경우는 따로 더하기
    else:
        value += int(x)
# 알파벳을 오름차순으로 정렬
result.sort()
# 숫자가 하나라도 존재하면 가능 뒤에 삽입
    