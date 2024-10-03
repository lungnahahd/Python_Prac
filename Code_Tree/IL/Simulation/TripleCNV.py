# 삼각형 컨베이어 벨트

import sys
input = sys.stdin.readline

size, time = list(map(int, input().split()))
plc = []
plain = []
for _ in range(3):
    temp = list(map(int, input().split()))
    plc.append(temp)
    for val in temp:
        plain.append(val)

while time > 0:
    before = plain[0]
    plain[0] = plain[-1]
    for idx in range(1,size*3):
        before, plain[idx] = plain[idx], before
    time -= 1

row = -1

for idx in range(size*3):
    if idx % size == 0 and idx != 0:
        print()
    print(plain[idx], end = ' ')

    
    #plc[row][idx % size] = plain[idx]
