# 코드네임
## 점수가 제일 낮은 요원의 코드네임과 점수를 출력

import sys
input = sys.stdin.readline

class GetInfo:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def showScore(self):
        return self.score
    def showCodeName(self):
        return self.name

secretMembers = []
for i in range(5):
    info = input().split()
    member = GetInfo(info[0],info[1])
    secretMembers.append(member)

lowId = 0
lowScore = 101
for i in range(5):
    if lowScore > int(secretMembers[i].showScore()):
        lowId = i
        lowScore = int(secretMembers[i].showScore())

print(secretMembers[lowId].showCodeName() + " " + secretMembers[lowId].showScore())