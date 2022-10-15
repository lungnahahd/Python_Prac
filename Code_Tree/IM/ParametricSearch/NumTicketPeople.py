# 번호표를 든 N명의 사람
## 테크닉 : 이진 탐색 활용



import sys
import heapq
INT_MAX = sys.maxsize

n,m = input().split()
peopleCount, limitTime = int(n), int(m)


time = []
for i in range(peopleCount):
    get = int(input())
    time.append(get)

left = 0
right = peopleCount 
ans = INT_MAX

# 해당 인원이 올라갔을 때, 주어진 시간 안에 해결 가능한지를 확인하는 함수
def check(num):
    save = []
    for i in range(num):
        heapq.heappush(save, time[i]) # 큐에 담기
    
    for i in range(num,peopleCount):
        small = heapq.heappop(save)
        small += time[i]
        heapq.heappush(save,small) # 가장 적은 시간을 가진 사람이 나오고 거기에 다음 사람이 들어오는 동작을 작성한 코드
    now = 0
    for i in save:
        now = max(now,i) # 현재 큐에서 최대값 찾기(큐는 최소값을 찾는 것만 바로 처리 가능)
    if now <= limitTime:
        return True
    else:
        return False


while left <= right:
    mid = (left + right) // 2
    if check(mid):
        ans = min(ans,mid)
        right = mid - 1
    else:
        left = mid + 1
print(ans)