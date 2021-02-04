count = int(input())

result = [0 for i in range(count)]
for i in range(count) :
    stair = int(input())
    room = int(input())
    
    people = [1 for i in range(room)]
    
    for m in range(stair + 1):
        for n in range(1,room):
            people[n] += people[n-1]
    result[i] = people[-1]
for j in range(count):
    print(result[j])