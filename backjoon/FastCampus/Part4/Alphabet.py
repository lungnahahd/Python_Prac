# 알파벳 (1987)
## 난이도 : 골드4

import sys
from collections import deque

input = sys.stdin.readline

now_visit = deque([])
row, col = list(map(int, input().split()))

alphabets = []
road_cost = []
meet_alphabet = set()
visited = [False] * 26
result = 0

for _ in range(row):
    temp = list(input())
    start_cost = [1 for _ in range(len(temp))]
    alphabets.append(temp)
    road_cost.append(start_cost)

def visiting(r,c, cost):
    global now_visit
    global alphabets
    global meet_alphabet
    global result 

    move_r = [-1,0,+1,0]
    move_c = [0,-1,0,+1]

    #meet_alphabet.add(alphabets[r][c])
    visited[ord(alphabets[r][c]) - 65] = True

    for idx in range(4):
        next_r,next_c = r + move_r[idx] , c + move_c[idx]
        if 0 <= next_r < row and 0 <= next_c < col:
            if visited[ord(alphabets[next_r][next_c]) - 65]:
            #if alphabets[next_r][next_c] in meet_alphabet:
                #result = max(result, len(meet_alphabet))
                result = max(result, cost)
            else:
                visited[ord(alphabets[next_r][next_c]) - 65] = True
                visiting(next_r, next_c, cost+1)
                visited[ord(alphabets[next_r][next_c]) - 65] = False
                #meet_alphabet.remove(alphabets[next_r][next_c])
visiting(0,0,1)
print(result)

