# 소수 찾기
## 숫자 리스트에서 소수를 찾는 코드

import math

nums = [True for _ in range(10000000)]
def solution(numbers):
    # 에라토스테네스의 체를 이용해서 소수를 구해내는 부분
    answer = 0
    nSize = len(numbers)
    temp = "9" * nSize
    temp = int(temp)
    for idx in range(2, int(math.sqrt(temp))):
        if nums[idx]:
            incre = 2
            while idx * incre <= temp:
                nums[idx*incre] = False
                incre += 1
    lstNums = list(numbers)
    # 생각을 전환해서 최대 범위 내에서 소수를 리스트로 했을 때, 해당 쪽지에 원소가 있는지를 확인
    for idx in range(2,temp):
        if nums[idx]:
            tempList = lstNums[:]
            tempIdx = list(str(idx))
            check = True
            for i in tempIdx:
                if i in tempList:
                    tempList.remove(i) # 원소를 하나씩 제거해주면서 확인
                else: # 만일 원소가 없다면 종료
                    check = False
                    break
            if check:
                answer += 1

    return answer

s = "17"
s = "011"
print(solution(s))