# 타켓 넘버 (Level 2)

result = 0

def solution(numbers, target):
    global result
    maxNum = 0
    answer = 0
    for i in numbers:
        maxNum += i
    if maxNum == target:
        answer = 1
    else:
        for i in range(len(numbers) - 1):
            if maxNum - numbers[i]*2 == target:
                result += 1
            checkSum(numbers,i,maxNum - 2*numbers[i], target)
        if maxNum - 2*numbers[-1] == target:
            result += 1
        answer = result
    return answer

# 반복적으로 들어가면서 타겟 넘버가 형성되는지 확인하는 부분
def checkSum(arr,where,sum,target):
    global result
    where += 1
    if where < len(arr):
        temp = sum - 2*arr[where]
        if where == len(arr) -1:
            if temp == target:
                result += 1
        else:
            if temp == target:
                result += 1
                checkSum(arr,where,sum,target)
            else:
                checkSum(arr,where,temp,target)
                checkSum(arr,where,sum,target)

#numbers = [1,1,1,1,1]
numbers = [4,1,2,1]
#target = 3
target = 4
num = [1,1,1,1,1]
t = 1
#print(solution(numbers,target))
print(solution(num,1))