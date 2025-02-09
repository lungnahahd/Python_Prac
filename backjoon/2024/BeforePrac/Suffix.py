# 접미사 배열 프로그램
## 접미사 배열 : 주어진 문자열의 모든 접미사를 사전순으로 정렬해 놓은 배열
## 여기서 말하는 접미사는 앞에서부터 한 글자씩 빼면서 나오는 단어들을 의미
### 입력 : 문자열이 주어지고, 모두 알파벳 소문자로 이루어져있으며, 길이는 1000을 넘지 않음
### 출력 : 접미사를 사전순으로 한 줄에 하나씩 출력

import sys
from collections import deque
input = sys.stdin.readline

getString = input()
getString = getString[:-1]
# 입력 받은 문장을 deque에 저장 -> popleft를 쓰기 위함
temp = deque(getString)
# 접미사 배열 생성
suffixArray = []
while len(temp) != 0:
    # deque의 내용을 문자열로 만들어서 접미사 배열에 저장
    stringSuffix = ''.join(temp)
    suffixArray.append(stringSuffix)
    # 새로운 접미사를 만들기 위해 popleft 활용
    temp.popleft()
# 접미사 배열을 알파벳 순으로 정렬하고 하나씩 출력하는 과정
suffixArray.sort()
for i in suffixArray:
    print(i)