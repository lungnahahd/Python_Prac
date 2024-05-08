# 상어 초등학교 (21608)
## 난이도 : 골드 5

import sys
import heapq
input = sys.stdin.readline

size = int(input())
student_order = []      # 자리를 배정할 학생의 순서를 저장하는 배열
want_dict = dict()      # 같이 앉길 원하는 학생들에 대한 정보를 저장하는 딕셔너리
where_dict = dict()     # 실제 위치가 정해진 학생에 대한 정보를 저장하는 딕셔너리
shark_class = [[0 for _ in range(size)] for _ in range(size)] # 인접 공간 중에 얼만큼의 자리가 남아 있는지를 저장하는 배열 


for _ in range(size*size):
    me, want_1, want_2, want_3, want_4 = list(map(int, input().split()))
    student_order.append(me)
    want_dict[me] = (want_1, want_2, want_3, want_4)

check_row = [-1, 0, +1, 0]
check_col = [0, +1, 0, -1]

for idx in range(size*size):
    now_student = student_order[idx]
    want_students = want_dict[now_student]
    able_sit = []
    for r in range(size):
        for c in range(size):
            if shark_class[r][c] != 0:
                continue
            blank = 0
            love = 0
            for i in range(4):
                next_r, next_c = r + check_row[i], c + check_col[i]
                if 0 <= next_r < size and 0 <= next_c < size:
                    if shark_class[next_r][next_c] == 0:
                        blank += 1
                    elif shark_class[next_r][next_c] in want_students:
                        love += 1
            heapq.heappush(able_sit, (-love, -blank, r, c))
    _, _, your_row, your_col = heapq.heappop(able_sit)
    shark_class[your_row][your_col] = now_student

result = 0
for r in range(size):
    for c in range(size):
        now_point = 0
        for i in range(4):
            next_r, next_c = r + check_row[i], c + check_col[i]
            if 0 <= next_r < size and 0 <= next_c < size:
                if shark_class[next_r][next_c] in want_dict[shark_class[r][c]]:
                    now_point += 1
        if now_point != 0:
            result += 10**(now_point - 1)

print(result)