# 스택 (10828)

cnt_cmd = int(input())
stack = []
result = []
for _ in range(cnt_cmd):
    cmd = input().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            result.append('-1')
        else:
            result.append(stack.pop())
    elif cmd[0] == 'top':
        if len(stack) == 0:
            result.append('-1')
        else:
            result.append(stack[-1])
    elif cmd[0] == 'size':
        result.append(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            result.append('1')
        else:
            result.append('0')
for rst in result:
    print(rst)