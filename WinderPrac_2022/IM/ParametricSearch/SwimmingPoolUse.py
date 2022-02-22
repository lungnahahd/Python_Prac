# 수영장 효율적으로 활용하기
## 테크닉 : 이진 탐색 응용



import sys
INT_MAX = sys.maxsize

n, m  = input().split()
peopleCount, railCount = int(n), int(m)

swimTime = list(map(int, input().split()))



left = 0
right = 1440 *peopleCount
#sum(swimTime)
ans = INT_MAX

def check(num):
    semiCheck = True # 정해진 num이라는 시간에 한 명도 수영을 완료할 수 없는 경우
    count = 0 # 현재 사용하는 레일을 카운트
    temp = 0 # 현재까지 한 레일에 얼마나 시간을 썼는지를 계산해주는 변수
    for i in swimTime:
        if i > num:
            semiCheck = False
            break
        temp += i
        
        if temp <= num:
            if count == 0:
                count += 1
        else:
            count += 1
            temp = i

    if count <= railCount :
        return semiCheck
    else:
        semiCheck = False
        return semiCheck



# 이진 탐색을 활용하는 코드
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

print(ans)