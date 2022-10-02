# 구명 보트

def solution(people, limit):
    answer = 0
    people = sorted(people)
    big,small = len(people)-1,0
    weight,save_num = 0,0
    while big > small:
        if weight == 0:
            weight += people[big]
            big -= 1
            save_num += 1

        if weight < limit:
            temp = weight+people[big]
            if temp <= limit:
                big -= 1
                save_num += 1
            else:
                temp = min(limit,weight+people[small])
                if weight+people[small] == limit or temp != limit:
                    small += 1
                    save_num += 1
            weight = temp

        weight = 0
        answer += 1

    if save_num != len(people):
        #print(small,big)
        answer += 1

    return answer

print(solution([70, 50, 80, 50],10000))
print(solution([70, 80, 50],100))