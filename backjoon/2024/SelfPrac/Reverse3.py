# 뒤집기3 (1464)
## 난이도 : 골드 4

s = list(input())

for idx in range(1,len(s)):
    if s[0] >= s[idx]:
        s = list(reversed(s[:idx]))+ s[idx:]
        s = list(reversed(s[:idx+1])) + s[idx+1:]
print(''.join(s))