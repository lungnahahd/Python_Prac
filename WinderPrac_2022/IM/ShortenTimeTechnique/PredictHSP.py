# 미래가 보이는 가위바위보
## A와 B가 가위바위보를 총 N회 진행합니다. A는 B가 무엇을 낼지 알고 있습니다
## A는 주먹, 가위, 보자기 중 같은 것을 연속해서 내고, 게임 N회 중 최대 한 번만 자신이 내는 것을 바꿔, 이후에는 바꾼 것을 계속 내려고 합니다.
## 예를 들어 K번 연속 주먹을 내고, N-K번은 가위를 냅니다.
## A가 이길 수 있는 게임 수의 최댓값을 구하는 프로그램을 작성해보세요.

gameCount = int(input())


bCase = []
for i in range(gameCount):
    case = input()
    bCase.append(case)

aPFront = [0 for i in range(gameCount)]
aPBack = [0 for i in range(gameCount)]
aHFront = [0 for i in range(gameCount)]
aHBack = [0 for i in range(gameCount)]
aSBack = [0 for i in range(gameCount)]
aSFront = [0 for i in range(gameCount)]

if bCase[0] == "P":
    aSFront[0] = 1
elif bCase[0] == "H":
    aPFront[0] = 1
else:
    aHFront[0] = 1

for i in range(1,gameCount):
    if bCase[i] == "P":
        aSFront[i] = aSFront[i-1] + 1
        aPFront[i] = aPFront[i-1]
        aHFront[i] = aHFront[i-1]
    elif bCase[i] == "H":
        aPFront[i] = aPFront[i-1] + 1
        aSFront[i] = aSFront[i-1]
        aHFront[i] = aHFront[i-1]
    else:
        aHFront[i] = aHFront[i-1] + 1
        aPFront[i] = aPFront[i-1]
        aSFront[i] = aSFront[i-1]

if bCase[gameCount-1] == "P":
    aSBack[gameCount-1] = 1
elif bCase[gameCount-1] == "H":
    aPBack[gameCount-1] = 1
else:
    aHBack[gameCount-1] = 1


for i in range(1,gameCount):
    if bCase[gameCount-1-i] == "P":
        aSBack[gameCount-1-i] = aSBack[gameCount - i] + 1
        aPBack[gameCount-1-i] = aPBack[gameCount - i]
        aHBack[gameCount-1-i] = aHBack[gameCount - i]
    elif bCase[gameCount-1-i] == "H":
        aPBack[gameCount-1-i] = aPBack[gameCount - i] + 1
        aSBack[gameCount-1-i] = aSBack[gameCount - i]
        aHBack[gameCount-1-i] = aHBack[gameCount - i]
    else:
        aHBack[gameCount-1-i] = aHBack[gameCount - i] + 1
        aPBack[gameCount-1-i] = aPBack[gameCount - i]
        aSBack[gameCount-1-i] = aSBack[gameCount - i]

maxH = max(aHFront)
maxP = max(aPFront)
maxS = max(aSFront)
totalMax = max(maxH,maxP,maxS)

# if maxH == totalMax:
#     where = aHFront.index(maxH)
#     if where != gameCount - 1:
#         back = max(aPBack[where+1],aSBack[where+1],aHBack[where+1])
#         totalMax += back
# elif maxP == totalMax:
#     where = aPFront.index(maxP)
#     if where != gameCount - 1:
#         back = max(aHBack[where+1],aSBack[where+1],aPBack[where+1])
#         totalMax += back
# else:
#     where = aSFront.index(maxS)
#     if where != gameCount - 1:
#         back = max(aPBack[where+1],aHBack[where+1],aSBack[where+1])
#         totalMax += back
# print(totalMax)
