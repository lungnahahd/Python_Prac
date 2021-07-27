# 소수 찾기 알고리즘
## 해당 자연수가 소수인가? -> 소수는 1과 자기자신을 제외한 어떤 수로도 나눌 수 없음
## 2부터 해당 수의 제곱근에 +1 한 수까지 나눠주면서 나누는 것이 가능하다면 소수가 아니고, 나누는 것이 불가능하다면 소수라고 볼 수 있다.

import math

num_check = input("소수 판별을 원하는 숫자를 입력해 주세요! : ")

half = int(math.sqrt((int(num_check)))) + 1

check = True
for i in range(2,half+1):
    if int(num_check) % i == 0 and int(num_check) != i:
        check = False
        break
if check:
    print("해당 수는 소수가 맞습니다.")
else:
    print("해당 수는 소수가 아닙니다.")