# 최장 공통 부분 수열

a_string = input()
b_string = input()

check_map = [[0 for _ in range(len(b_string) + 1)] for _ in range(len(a_string) + 1)]

for a in range(1, len(a_string)+1):
    for b in range(1,len(b_string)+1):
        check_map[a][b] = check_map[a-1][b]
        if a_string[a-1] == b_string[b-1]:
            check_map[a][b] = check_map[a-1][b-1] + 1
        check_map[a][b] = max(check_map[a][b-1], check_map[a][b])
            
print(check_map[-1][-1])