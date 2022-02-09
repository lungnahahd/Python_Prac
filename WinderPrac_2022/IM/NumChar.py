# 대응되는 수와 문자
# 해시를 사용하는 이유 : 단순 검색만 필요하고, 리스트로 처리하기에는 시간 복잡도 문제 발생 가능
# import sys
# input = sys.stdin.readline

cmd = list(map(int,input().split()))

d = dict()
reverseD = dict()

for i in range(cmd[0]):
    a = input()
    b = a.strip()
    d[b] = i+1
    reverseD[i+1] = b

for i in range(cmd[1]):
    find = input()
    if find.isdigit():
        print(reverseD[int(find)])
    else:
        print(d[find])
    