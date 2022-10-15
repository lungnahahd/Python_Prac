# 특별한 문자
## 소문자 알파벳으로만 이루어져 있는 문자열이 하나 주어졌을 때, 해당 문자열에 단 한번만 나오는 문자를 찾는 프로그램을 작성해보세요.
### 해시 사용 이유 : 정렬을 할 필요가 없고, 알파벳 별로 계속 조회를 해야하므로 해사 사용

speacial = input()
speacial = list(speacial)

coundDic = dict()

for i in range(len(speacial)):
    if speacial[i] in coundDic:
        coundDic[speacial[i]] += 1
    else:
        coundDic[speacial[i]] = 1

noEnd = True
for i in range(len(speacial)):
    if coundDic[speacial[i]] == 1:
        print(speacial[i])
        noEnd = False
        break
if noEnd:
    print("None")