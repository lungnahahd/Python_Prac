# 최대 점프 가능 횟수
## 최대 점프 크기가 표기된 리스트에서 점프할 때, 시작점(0)에서 할 수 있는 가장 많은 점프 횟수 구하기
##### DP 문제로 풀이하다가 시간 초과 발생 -> visited 리스트를 이용해서 중복 검사를 하는 과정을 제거해서 해결
##### 리스트로 queue를 이용할 경우, pop()을 이용해서는 가장 뒤에 원소가 삭제됨을 인지 -> pop(0) 을 해야 맨 앞에 원소 삭제


n = int(input())
num_arr = list(map(int, input().split()))
result = [0 for _ in range(n)] # 결과를 담는 리스트
visited =  [False for _ in range(n)] # 시간 초과 문제를 해결하기 위해 선 확인 하는 리스트

can_move = [] # 갈 수 있는 노드 인덱스를 담아 둘 큐 리스트
can_move.append(0)

while can_move:
    node = can_move.pop(0)
    max_jump = num_arr[node]
    for jump in range(1,max_jump+1):
        if(node + jump < n ):
            result[node+jump] = max(result[node+jump], result[node] + 1)
            if (not visited[node+jump]):
                can_move.append(node+jump)
                visited[node+jump] = True

print(max(result))
