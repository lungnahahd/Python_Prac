# 알파벳 (1987)
## 난이도 : 골드4

import sys

input = sys.stdin.readline

row, col = list(map(int, input().split()))

alphabets = []
meet_alphabet = set()
result = 0
move_r = [-1,+1,0,0]
move_c = [0,0,-1,+1]

for _ in range(row):
    temp = list(input())
    alphabets.append(temp)

def visiting(r,c, cost):
    global alphabets, meet_alphabet, result

    result = max(result, cost)

    for idx in range(4):
        next_r,next_c = r + move_r[idx] , c + move_c[idx]
        if 0 <= next_r < row and 0 <= next_c < col:
            if alphabets[next_r][next_c] not in meet_alphabet:
                meet_alphabet.add(alphabets[next_r][next_c])
                visiting(next_r, next_c, cost+1)
                meet_alphabet.remove(alphabets[next_r][next_c])

meet_alphabet.add(alphabets[0][0])
visiting(0,0,1)

print(result)

