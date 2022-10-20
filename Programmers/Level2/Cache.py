# 캐시

def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        answer += 5*(len(cities))
    else:
        for city in cities:
            if city.upper() in cache:
                answer += 1
                cache.remove(city.upper())
            else:
                answer += 5
                if len(cache) == cacheSize:
                    cache.pop()
            cache.insert(0,city.upper())


    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(4,["Jeju", "Pangyo", "NewYork", "newyork"]))