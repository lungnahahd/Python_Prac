# 서로 다른 k개의 문자
## 문자열 한 개가 입력으로 주어졌을 때 해당 문자열에 포함된 연속한 부분 문자열 중 해당 문자열 내의 서로 다른 문자의 수가 k개를 넘지 않는 경우 중 가장 긴 부분 문자열의 길이를 구하는 코드를 작성해보세요.
### 테크닉 : Two Pointer 테크닉


import sys
INT_MAX = sys.maxsize

get, num = input().split()
getStr, num = list(get),int(num)

check = 0 # 해당 위치에서 서로 다른 문자가 몇 개인지 확인하는 것
start = 0 # 변하는 시작점을 기록하는 변수
save = dict() # 서로 다른 문자의 위치를 기록
result = 0 # 가장 긴 문자열의 길이

for i in range(len(getStr)):
    nowWord = getStr[i]
    # 서로 다른 문자를 dict()로 관리
    if nowWord not in save:
        if len(save) == num:
            distance = i - start
            result = max(result, distance)
            # 가장 가까운 서로 다른 점 부분을 시작점으로 지정
            start = min(save.values()) + 1
            # 가장 시작점에서 가까웠던 점을 제거
            # value를 이용해서 key를 찾고 제거
            for key, value in save.items():
                if value == start-1:
                    save.pop(key)
                    break
        # 현재의 값을 넣기
        save[nowWord] = i
    else:
        # 항상 해당 문자의 위치를 가장 시작점에서 멀리 있는 것으로 기록
        save[nowWord] = i
# 마지막으로 거리를 갱신       
lastDistance = len(getStr) - start
result = max(result,lastDistance)

print(result)