import sys
input = sys.stdin.readline
# 숫자 결과를 담는 변수
alphabetNum = [0 for i in range(26)]
# 단어 입력 받고 그걸 리스트에 넣기
get = input()
get = list(get)[:-1]
for i in get:
    num = ord(i) - 97
    alphabetNum[num] += 1
for i in alphabetNum:
    print(i, end=' ')