# k개 중에 1개를 n번 뽑기

k, n = map(int,input().split())

save_num = []

def bt():
    global save_num

    for i in range(1,k+1):
        if len(save_num) == n:
            result = ''
            for j in save_num:
                result += str(j)
                result += " "
            print(result)
            return
        else:
            save_num.append(i)
            bt()
            save_num.pop()



bt()