# 오등큰수
## 주어진 수열에서 각 자릿수와 같은 수가 몇번 나오는지 나태나는 배열이 있을 때,
## 해당 자리의 오른쪽에서 자신보다 빈도수가 많은 것이 있으면 그 수가 해당 자릿수의 결과가 되고,
## 없다면 -1 이 해당 결과가 된다. 
### 첫 줄에 수열의 크기와 두번째 줄에 해당 수열이 주어지게 된다.

import sys
input = sys.stdin.readline
# 수열의 크기를 받는 부분
size = int(input())
# 숫자 배열을 받는 부분
num_list = input().split()
numArray = []
for i in range(size):
    numArray.append(int(num_list[i]))
# 빈도수 배열을 만드는 부분
freq = [0 for i in range(max(numArray) + 1)]
#freq = [1 for i in range(size)]
for i in range(size):
    freq[numArray[i]] += 1
#  빈도수 배열에 따라서 오등큰수를 처리하는 부분
result = [-1 for i in range(size)]
tempSave = []
tempSave.append(0)
for i in range(1, size):
    for j in range(len(tempSave)):
        if freq[tempSave[-1]] < freq[i]:
            result[tempSave.pop()] = freq[numArray[i]]
        else:
            break
    tempSave.append(i)
    
for i in range(size):
    print(result[i],end=' ')