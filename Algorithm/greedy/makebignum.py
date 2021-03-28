# 각자리의 숫자(0~9) 로만 구성된 문자열이 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩
# 모든 숫자를 확인하면서 숫자 사이에 'x' 혹은 '+' 연산자를 사용해서 결과적으로
# 만들어 질 수 있는 가장 큰 수를 구하는 프로그램 작성
import sys
input = sys.stdin.readline

get = input().strip()
size = len(get)
num = [0 for i in range(size)]
resultnum = 0

for i in range(len(get)):
    if int(get[i]) == 1 or int(get[i]) == 0 or resultnum == 0:
        resultnum = resultnum + int(get[i])
    else:
        resultnum = resultnum * int(get[i])
print(resultnum)