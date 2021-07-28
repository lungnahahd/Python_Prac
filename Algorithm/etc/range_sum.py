# 구간합 빠르게 구하기 알고리즘
## 특정 구간의 모든 수를 합한 결과를 구하는것으로 특정 구간을 말하면 그 여러 구간들의 합을 출력
### 숫자 쌍을 여러 개 제공
### 먼저 인덱스 0일 때부터 차례로 증가하면서 누적 합을 구하고, 원하는 구간 합을 단순히 누적 합을 빼주면서 구하기

wantcount = input("원하는 구간의 갯수를 입력하시오 : ")
wantcount = int(wantcount)

end = 0
array = [1,2,3,2,5]
sumarray = []
sum = 0
while end < len(array):
    sum += array[end]
    sumarray.append(sum)
    end += 1

print(sumarray)

for i in range(wantcount):
    startPointer, endPointer = map(int, input().split())
    result = sumarray[endPointer] - sumarray[startPointer - 1]
    print(result)