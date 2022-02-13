# 구간에 속한 문자의 개수
## n x m 크기의 2차원 격자가 알파벳 소문자 a, b, c 로만 이루어져 있습니다.
## k개의 질의에 대해 주어진 직사각형 범위 안에 각각 a b c 가 몇 개씩 있는지를 구하는 프로그램을 작성해보세요.

n,m,k = input().split()
n = int(n)
m = int(m)
k = int(k)

prefix = [[[0,0,0] for i in range(m+1)] for j in range(n+1)]

stringArr = []
for i in range(n):
    get = list(input())
    stringArr.append(get)


for i in range(1,n+1):
    for j in range(1,m+1):
        if stringArr[i-1][j-1] == "a":
            prefix[i][j][0] = prefix[i-1][j][0] + prefix[i][j-1][0] - prefix[i-1][j-1][0] + 1
            prefix[i][j][1] = prefix[i-1][j][1] + prefix[i][j-1][1] - prefix[i-1][j-1][1]
            prefix[i][j][2] = prefix[i-1][j][2] + prefix[i][j-1][2] - prefix[i-1][j-1][2]
        elif stringArr[i-1][j-1] == "b":
            prefix[i][j][1] = prefix[i-1][j][1] + prefix[i][j-1][1] - prefix[i-1][j-1][1] + 1
            prefix[i][j][0] = prefix[i-1][j][0] + prefix[i][j-1][0] - prefix[i-1][j-1][0]
            prefix[i][j][2] = prefix[i-1][j][2] + prefix[i][j-1][2] - prefix[i-1][j-1][2]
        else:
            prefix[i][j][2] = prefix[i-1][j][2] + prefix[i][j-1][2] - prefix[i-1][j-1][2] + 1
            prefix[i][j][0] = prefix[i-1][j][0] + prefix[i][j-1][0] - prefix[i-1][j-1][0]
            prefix[i][j][1] = prefix[i-1][j][1] + prefix[i][j-1][1] - prefix[i-1][j-1][1]

for i in range(k):
    r1, c1, r2, c2 = input().split()
    r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
    print(prefix[r2][c2][0]-prefix[r1-1][c2][0]-prefix[r2][c1-1][0] + prefix[r1-1][c1-1][0] , end=' ')
    print(prefix[r2][c2][1]-prefix[r1-1][c2][1]-prefix[r2][c1-1][1] + prefix[r1-1][c1-1][1], end=' ')
    print(prefix[r2][c2][2]-prefix[r1-1][c2][2]-prefix[r2][c1-1][2] + prefix[r1-1][c1-1][2])