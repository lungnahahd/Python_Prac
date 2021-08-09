# 단어 길이 재기
## 알파벳으로만 이루어진 단어를 입력 받고, 그 길이를 출력하는 프로그램
### 입력 : 소문자와 대문자로만 구성된 단어 입력 (단어의 길이는 최대 100)
### 출력 : 입력으로 주어진 단어의 길이를 출력

import sys
input = sys.stdin.readline

word = input()
print(len(word) - 1)