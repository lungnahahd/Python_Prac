# 수 찾기 (1920)

origin_num = int(input())
origin_set = set(map(int, input().split()))
find_num = int(input())
find_list = list(map(int, input().split()))

answer = []

for find in find_list:
    if find in origin_set:
        print(1)
    else:
        print(0)