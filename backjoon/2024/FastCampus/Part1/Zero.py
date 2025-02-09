# 제로 (10773)

cnt = int(input())
stack = []
result = 0

for _ in range(cnt):
    now_int = int(input())
    if now_int == 0:
        stack.pop()
    else:
        stack.append(now_int)

while stack:
    result += stack.pop()

print(result)