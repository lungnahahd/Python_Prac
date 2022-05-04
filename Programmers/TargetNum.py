# 타켓 넘버 (Level 2)



result = 0


def solution(numbers, target):
    global result
    maxNum = 0
    answer = 0
    for i in numbers:
        maxNum += i
    diff = maxNum - target
    if diff % 2 == 0:
        diff = diff / 2
        for i in range(len(numbers) - 1):
            if maxNum - numbers[i]*2 == target:
                result += 1
            checkSum(numbers,i,diff,maxNum - 2*numbers[i], target)
            #print("====>" + str(result))
        if maxNum - 2*numbers[-1] == target:
            result += 1
        answer = result
    return answer

def checkSum(arr,where,stand,sum,target):
    global result
    where += 1
    #print(where)
    if where < len(arr):
        temp = sum - 2*arr[where]
        if where == len(arr) -1:
            #temp = sum - 2*arr[where]
            if temp == target:
                result += 1
        #elif temp >= stand:
        else:
            #temp = sum - 2*arr[where]
            if temp == target:
                result += 1
            else:
                checkSum(arr,where,stand,temp,target)
                checkSum(arr,where,stand,sum,target)

#numbers = [1,1,1,1,1]
numbers = [4,1,2,1]
#target = 3
target = 4
print(solution(numbers,target))