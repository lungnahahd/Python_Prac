# Next Level
## "아이디"와 "레벨"을 같이 저장할 수 있는 형태

import sys
input = sys.stdin.readline

class GetInfo:
    def __init__(self,id = "codetree",level = "10"): # 객체 생성시 기본 값 부여
        self.id = id
        self.level = level
    
    def showUser(self):
        print("user " + self.id + " lv " + self.level)

newInfo = input().split()

baseUser  = GetInfo() # 매개변수 초기 값을 그대로 사용
newUser = GetInfo(newInfo[0],newInfo[1]) # 매개변수 값을 입력으로 변경

baseUser.showUser()
newUser.showUser()