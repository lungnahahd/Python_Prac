# 쪼개어 배낭 채우기 구현
## 테크닉 : 그리디 알고리즘

n, m = input().split()
jewelry, bag = int(n), int(m)


save = [] # 쪼갠 보석의 가치를 저장하는 리스트

for i in range(jewelry):
    w,v = input().split()
    weight,value = int(w),int(v)
    save.append((-(value/weight),weight))

save.sort()
result = 0
# 쪼갠 보석을 가방에 담는 코드
for value,weight in save:
    if bag - weight >= 0:
        result += -value*(weight)
        bag -= weight
    else:
        result += -value*bag
        break

print("{:.3f}".format(result)) # 소숫점 3자리까지 출력