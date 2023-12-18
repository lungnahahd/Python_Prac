# 키로거 (5397)

case_cnt = int(input())
answer = []

for _ in range(case_cnt):
    now_pwd = []
    temp_pwd = []
    procedure = input()
    cursur = 0
    for step in procedure:
        if (step == '<'):
            if (len(now_pwd) != 0):
                temp = now_pwd.pop()
                temp_pwd.append(temp)
        elif (step == '>'):
            if (len(temp_pwd) != 0):
                temp = temp_pwd.pop()
                now_pwd.append(temp)
        elif (step == '-'):
            if (len(now_pwd) != 0):
                now_pwd.pop()
        else:
            now_pwd.append(step)
    now_pwd.extend(reversed(temp_pwd))
    answer.append(''.join(now_pwd))

for show in answer:
    print(show)