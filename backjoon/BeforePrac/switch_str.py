import sys
input = sys.stdin.readline
num = input()
num = int(num)
#words = [0 for i in range(1001)]
count = 0

while count != num:
    words = map(str,input().split())
    strlist = list(words)
    #print(' '.join(strlist))
    for i in range(len(strlist)):
        temp = [0 for j in range(len(strlist[i]) + 1)]
        for n in range(len(strlist[i])):
            temp[n] = strlist[i][len(strlist[i]) - n - 1]
        temp[len(temp) - 1] = " "
        strlist[i] = "".join(temp)
    print(''.join(strlist))

    count += 1




