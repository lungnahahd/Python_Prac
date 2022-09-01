# 이상한 수열(코드 트리)

from pickletools import read_unicodestring1


n = int(input())

def makeArr(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return makeArr(n//3) + makeArr(n-1)


print(makeArr(n))