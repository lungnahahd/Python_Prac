# ROT13 암호 프로그램
## 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만드는 프로그램
## 특정 문장을 ROT13 암호화하고 다시 이를 되돌리는 경우에도 다시 ROT13을 진행하면 복호화 가능
## ROT13은 알파벳 대,소문자에만 적용 가능하고 그 외에 숫자에는 적용하지 않고 그대로 둔다
### 입력 : 알파벳 대,소문자와 공백, 숫자로 이루어진 문자열이 입력으로 제공 (길이는 100을 넘지 않음)
### 출력 : 입력을 ROT13 암호화한 내용을 출력

import sys
input = sys.stdin.readline

getString = input()
getString = getString[:-1]
result = ""
for i in getString :
    if i.isupper():
        num = ord(i) + 13
        if num > 90:
            num -= 26
        result += chr(num)
    elif i.islower():
        num = ord(i) + 13
        if num > 122:
            num -= 26
        result += chr(num)
    else:
        result += i

print(result)