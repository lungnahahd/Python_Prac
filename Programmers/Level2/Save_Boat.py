# 구명 보트

def solution(people, limit):
    answer = 0
    people = sorted(people) # 크기 순대로 정렬
    big,small = len(people)-1,0
    weight,save_num = 0,0
    while big > small: 
        # 보트가 비어있는 경우, 가장 무거운 사람부터 탑승
        if weight == 0:
            weight += people[big]
            big -= 1
            save_num += 1
        # 더 탑승할 수 있는 경우 실행
        if weight < limit:
            temp = weight+people[big]
            # 남아있는 사람 중 무거운 사람이 탑승할 수 있는 경우
            if temp <= limit:
                big -= 1
                save_num += 1
            # 남아있는 사람 중 가벼운 사람탑승
            else:
                temp = weight+people[small]
                if temp <= limit:
                    small += 1
                    save_num += 1
            weight = temp

        weight = 0
        answer += 1

    # 딱 한 사람이 구출되지 않은 경우 구명보트 추가
    if save_num != len(people):
        answer += 1

    return answer

print(solution([70, 50, 80, 50],10000))
print(solution([70, 80, 50],100))