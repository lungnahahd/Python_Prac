# 한 마을에 모험가가 N명 있을때, N명의 모험가를 대상으로 '공포도'를 측정
# 공포도가 X인 모험가는 X으로 구성한 모험가 그룹에 참여해야 그룹 결성 완료
# N명의 모험가에 대해 여행을 떠날 수 있는 그룹 수의 최댓값을 구하라
# N과 그에 해당하는 공포도는 주어지는 문제
# 몇 명의 모험가는 마을에 그대로 남아있어도 되기에 모든 모험가를 구룹에 넣을 필요는 없음

import sys
input = sys.stdin.readline

people = input().strip()
people = int(people)
bravelist = input().strip()
brave = [0 for i in range(people)]
#group = []
group = 0
count = 0
result = 0
for i in range(people):
        brave[i] = int(bravelist[count])
        count += 2
brave.sort()

for i in range(people):
    check = brave[i]
    group += 1
    if group == check:
        group = 0
        result += 1
print(result)