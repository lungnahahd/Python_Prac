# 보물 (1026)
## 난이도 : 실버 4

cnt = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

answer = 0

for idx in range(cnt):
    answer += (a[idx] * b[idx])

print(answer)