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

