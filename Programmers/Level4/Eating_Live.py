def solution(food_times, k):
    answer = 0
    ate = [0 for _ in range(len(food_times))]
    food_kind = len(food_times)
    now_food = 0
    fin = [False for _ in range(len(food_times))]
    
    while k != 0 and False in fin:
        ate[now_food] += 1
        if ate[now_food] == food_times[now_food]:
            fin[now_food] = True
        k -= 1
        now_food += 1
        if now_food == food_kind:
            now_food = 0
        while fin[now_food]:
            now_food += 1
            if now_food == food_kind:
                now_food = 0
    print(now_food)
    print(ate)
    print(fin)
    if False in fin:
        answer = now_food + 1
        if answer > food_kind:
            answer = 0
            while fin[answer]:
                answer += 1
            answer += 1
    else:
        answer = -1
        
        
        
        
    
    return answer