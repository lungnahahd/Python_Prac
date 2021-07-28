# 투 포인터 알고리즘
## 리스트에 순차적으로 접근할 때, 두 개의 포인터의 위치를 기록하면서 처리하는 알고리즘
### 시작점과 끝점을 명시해서 진행(접근 범위를 표현)
### 이를  활용해서 주어진 수열에서 특정 합이 N인 연속 수열의 갯수 구하기 가능
#### 시작 포인트와 끝 포인트를 0으로 두고 시작하면서 시작점에서 끝점의 합이 찾는 것과 같다면 결과치를 하나 증가
#### 찾는 것보다 작다면 끝 포인트를 하나 증가하고 크다면 시작 포인트를 하나 증가시키면서 알고리즘을 진행
#### 위의 과정을 더 이상 진행할 수 없을 때까지 진행한다면 최적의 해를 얻을 수 있음

want = input("원하는 구간 합을 입력하시오 : ")
wantsum = int(want)

array = [1,2,3,2,5]

startPointer = 0
endPointer = 0
count = 0

for i in range(wantsum):
    if startPointer == endPointer:
        check = array[startPointer]
    else:
        check = array[startPointer] + array[endPointer]
        if wantsum > check:
            endPointer += 1
        elif wantsum < check:
            startPointer += 1
        else:
            count += 1
    if startPointer > endPointer or endPointer > wantsum:
        break
print(count)