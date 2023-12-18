# 키로거 (5397)

case_cnt = int(input())
answer = []

for _ in range(case_cnt):
    now_pwd = []
    procedure = input()
    cursur = 0
    for step in procedure:
        if (step == '<'):
            if (cursur != 0):
                cursur -= 1
        elif (step == '>'):
            if (cursur < len(now_pwd)):
                cursur += 1
        elif (step == '-'):
            if (cursur != 0):
                now_pwd.pop(cursur-1)
                cursur -= 1
        else:
            if (cursur == len(now_pwd)):
                now_pwd.append(step)
            else:
                now_pwd.insert(cursur, step)
            cursur += 1
    answer.append(''.join(now_pwd))

for show in answer:
    print(show)