# 중복되지 않는 가장 긴 문자열
## 문자열 한 개가 입력으로 주어졌을 때 해당 문자열에 포함된 연속한 부분 문자열 중 중복되는 문자가 없는 가장 긴 부분 문자열을 구하는 코드를 작성해보세요.
### 테크닉 : Two Pointer 테크닉


getStr = list(input())

resultDistance = 1
save = dict() # 현재 해당 알파벳의 인덱스를 담는 변수
start = 0 # 변경되는 시작점을 기록 변수
idx = 0 # 앞으로 나가는 인덱스 기록 변수
while idx < len(getStr):
    standardWord = getStr[idx]
    if standardWord not in save:
        save[standardWord] = idx
    else:
        tempArr = getStr[start:idx]
        if standardWord not in tempArr:
            save[standardWord] = idx
        else:
            tempDistance = idx - start
            resultDistance = max(resultDistance,tempDistance)
            start = save[standardWord] + 1
            save[standardWord] = idx 
    idx +=1
    if idx == len(getStr):
        tempDistance = idx - start
        resultDistance = max(resultDistance, tempDistance)
print(resultDistance)