# 007
## "비밀 코드", "접선 장소", "시간" 이 입력되면, 이를 class로 저장하고 출력

import sys
input = sys.stdin.readline

class SaveInfo:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time
    
    def showInfo(self):
        print("secret code : " + self.code)
        print("meeting point : " + self.point)
        print("time : " + self.time)

getInfo = input().split()

secretMember = SaveInfo(getInfo[0],getInfo[1],getInfo[2])
secretMember.showInfo()

