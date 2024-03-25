# 알파벳 (1987)
## 난이도 : 골드4


import sys
from collections import deque

now_visit = deque([])
row, col = list(map(int, input().split()))

alphabets = []
meet_alphabet = set()
result = 0

for _ in range(row):
    temp = list(input())
    alphabets.append(temp)

def visiting(r,c):
    global now_visit
    global alphabets
    global meet_alphabet
    global result

    move_r = [-1,0,+1,0]
    move_c = [0,-1,0,+1]

    now_visit.append(alphabets[r][c])
    meet_alphabet.add(alphabets[r][c])


    for idx in range(4):
        next_r,next_c = r + move_r[idx] , c + move_c[idx]
        if 0 <= next_r < row and 0 <= next_c < col:
            if alphabets[next_r][next_c] in meet_alphabet:
                result = max(result, len(meet_alphabet))
            else:
                visiting(next_r, next_c)
                meet_alphabet.remove(alphabets[next_r][next_c])
                now_visit.pop()
visiting(0,0)
print(result)

