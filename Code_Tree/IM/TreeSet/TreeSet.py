# TreeSet
## sortedcontainers 외부 라이브러리 이용

from sortedcontainers import SortedSet
import sys
input = sys.stdin.readline

caseNum = int(input())

s = SortedSet() # 빈 treeSet 생성
for i in range(caseNum):
    case = input().split()
    if case[0] == "add":
        s.add(int(case[1]))
    elif case[0] == "find":
        if int(case[1]) not in s:
            print("false")
        else:
            print("true")
    elif case[0] == "remove":
        s.remove(int(case[1]))
    elif case[0] == "largest":
        if len(s) == 0:
            print("None")
        else:
            print(s[-1])
    elif case[0] == "smallest":
        if len(s) == 0:
            print("None")
        else:
            print(s[0])
    elif case[0] == "upper_bound":
        if s.bisect_right(int(case[1])) >= len(s):
            print("None")
        else:
            index = int(s.bisect_right(int(case[1])))
            print(s[index])
    elif case[0] == "lower_bound":
        if s.bisect_right(int(case[1])) >= len(s):
            print("None")
        else:
            index = int(s.bisect_left(int(case[1])))
            print(s[index])