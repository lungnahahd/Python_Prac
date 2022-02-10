# hashset
## 리스트와 달리 순서가 없고, 중복 데이터 허용 X
## 삽입, 삭제, 조회에서 시간 복잡도는 O(1)

import sys
input = sys.stdin.readline

caseSize = int(input())

def add(s,value):
    s.add(value)

def find(s,value):
    if value in s:
        print("true")
    else:
        print("false")

def remove(s,value):
    s.remove(value)

set = set() # 빈 딕셔너리 생성
for i in range(caseSize):
    case = input().split()
    if case[0] == "add":
        add(set,int(case[1]))
    elif case[0] == "remove":
        remove(set,int(case[1]))
    elif case[0] == "find":
        find(set,int(case[1]))
    