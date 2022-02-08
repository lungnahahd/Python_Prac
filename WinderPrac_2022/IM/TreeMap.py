# TreeMap 기본
## 균형 잡힌 이진트리 구조로 숫자들을 관리하는 자료구조
## key와 value로 저장되고, key를 기준으로 노드의 위치가 결정
### 파이썬에서는 sortedcontainers 외부 라이브러로 사용 가능

from sortedcontainers import SortedDict
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

def printList(dic):
    result = []
    if len(dic) == 0:
        print("None")
    else:
        for key, value in dic.items():
            print(value,end=' ')
        print()

caseSize = int(input()) # 수행할 명령어의 숫자

sd = SortedDict() # treemap 구현
for i in range(caseSize):
    case = input().split()
    if case[0] == "add":
        add(sd,int(case[1]),int(case[2]))
    elif case[0] == "remove":
        remove(sd,int(case[1]))
    elif case[0] == "find":
        find(sd,int(case[1]))
    elif case[0] == "print_list":
        printList(sd)
