# 이상한 수열(코드 트리)

n = int(input())

num_array = [0,1,2]

def makeArr(na):
    global n
    if n == 1 or n == 2:
        return na[n]
    one = na[(len(na) // 3)]
    two = na[len(na)-1]
    na.append(one+two)
    if len(na) == n+1:
        return na[-1]
    else:
        return makeArr(na)
print(makeArr(num_array))