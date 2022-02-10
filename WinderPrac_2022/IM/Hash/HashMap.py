# HashMap 기본

import sys
input = sys.stdin.readline


def add(dic,key, value): # 딕셔너리에 키와 값을 추가하는 함수
    dic[key] = value

def find(dic,key): # 딕셔너리에 주어진 키에 해당하는 값을 출력하는 함수
    if key in dic:
        print(dic[key])
    elif key not in dic:
        print("None")

def remove(dic,key): # 딕셔너리에 주어진 키에 해당하는 값을 제거하는 함수
    dic.pop(key)



caseSize = int(input()) # 수행할 명령어의 숫자

dic = dict() # 빈 딕셔너리 생성
for i in range(caseSize):
    case = input().split()
    if case[0] == "add":
        add(dic,int(case[1]),int(case[2]))
    elif case[0] == "remove":
        remove(dic,int(case[1]))
    elif case[0] == "find":
        find(dic,int(case[1]))
