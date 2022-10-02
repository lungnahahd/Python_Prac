# 주식 가격
## 초 단위로 주어지는 가격에서 하락인지 성공인지 확인

def solution(prices):
    answer = [-1] * len(prices)
    save_time = [0] # 지나는 시간을 담을 스택
    for time in range(1,len(prices)):
        while True:
            # 가격이 오른 경우
            if len(save_time) == 0 or prices[save_time[-1]] <= prices[time]:
                save_time.append(time) 
                break
            else: # 가격이 오르지 않은 경우
                temp_time = save_time.pop()
                answer[temp_time] = time - temp_time
    while save_time: # 모든 경우를 파악하고 최종 출력!
        temp_time = save_time.pop()
        answer[temp_time] = len(prices) - 1 - temp_time

    return answer

print(solution([4,2,3,2,3]))