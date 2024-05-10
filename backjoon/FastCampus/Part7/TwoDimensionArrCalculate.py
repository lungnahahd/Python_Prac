# 이차원 배열과 연산 (17140)
## 난이도 : 골드 4

import sys
import heapq
input = sys.stdin.readline

want_row, want_col, want_value = list(map(int, input().split()))
want_row -= 1
want_col -= 1

arr = []
time = 0
for _ in range(3):
    temp = list(map(int, input().split()))
    arr.append(temp)


def r_method(array):
    max_len = 0
    for row in range(len(array)):
        temp  = array[row]
        temp.sort()
        cnt, before = 0, temp[0]
        hq = []
        for num in temp:
            if num == 0:
                continue
            if num == before:
                cnt += 1
            else:
                if before != 0:
                    heapq.heappush(hq, (cnt, before))
                before = num
                cnt = 1
        heapq.heappush(hq, (cnt, before))
        mid_reslt = []
        while hq:
            cnt, num = heapq.heappop(hq)
            mid_reslt.append(num)
            mid_reslt.append(cnt)
        array[row] = mid_reslt
        max_len = max(max_len, len(mid_reslt))
    for row in array:
        if len(row) != max_len:
            for _ in range(len(row), max_len):
                row.append(0)
    return array

def trasport(array):
    origin_row, origin_col = len(array), len(array[0])
    trasport = [[0 for _ in range(origin_row)] for _ in range(origin_col)]
    for r in range(origin_row):
        for c in range(origin_col):
            trasport[c][r] = array[r][c]
    return trasport


def c_method(array):
    max_len = len(array) * 2
    mid_result = [[] for _ in range(max_len)]
    #mid_result = []

    cut = 0
    for col_idx in range(len(array[0])):
        now_col_arr = []
        for row_idx in range(len(array)):
            now_col_arr.append(array[row_idx][col_idx])
        now_col_arr.sort()
        cnt, before = 0, now_col_arr[0]
        hq = []
        for num in now_col_arr:
            if num == 0:
                continue
            if num == before:
                cnt += 1
            else:
                if before !=0 :
                    heapq.heappush(hq, (cnt, before))
                cnt = 1
                before = num
        heapq.heappush(hq, (cnt, before))
        end = 0
        while hq:
            if len(hq) == 0:
                mid_result[end].append(0)
                mid_result[end+1].append(0)
            else:
                cnt, num = heapq.heappop(hq)
                mid_result[end].append(num)
                mid_result[end+1].append(cnt)
            end += 2
        cut = max(cut, end)
    
    #mid_result = mid_result[:cut]

    return mid_result

#print(c_method(r_method(arr)))
#print(arr)
if arr[want_row][want_col] == want_value:
    print(time)
else:
    while time < 101:
        if len(arr) >= len(arr[0]):
            arr = r_method(arr)
        else:
            arr = trasport(arr)
            arr = r_method(arr)
            arr = trasport(arr)
            #arr = c_method(arr)
        time += 1
        if len(arr) > 100:
            arr = arr[:100]
        if len(arr[0]) > 100:
            for idx in range(len(arr)):
                arr[idx] = arr[idx][:100]
        if want_row < len(arr) and want_col < len(arr[0]):
            if (arr[want_row][want_col] == want_value):
                break
    

    if time > 100:
        print(-1)
    else:
        print(time)