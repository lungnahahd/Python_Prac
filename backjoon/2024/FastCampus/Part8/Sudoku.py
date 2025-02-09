# 스도쿠 (2580)
## 난이도 : 골드 4

import sys
input = sys.stdin.readline

sudoku_map = []
count_zero = 0
for _ in range(9):
    row = list(map(int, input().split()))
    for num in row:
        if num == 0:
            count_zero += 1
    sudoku_map.append(row)



def check_col(c, num):
    isYes = True
    for row in range(9):
        if sudoku_map[row][c] == num:
            isYes = False
            break
    return isYes

def check_row(r,num):
    isYes = True
    for col in range(9):
        if sudoku_map[r][col] == num:
            isYes = False
            break
    return isYes

def check_area(r,c,num):
    isYes = True
    #print(r,r//3, c,c//9)
    for row in range(r//3 * 3, r//3 * 3 + 2):
        for col in range(c//3 * 3, c//3 * 3 +2):
            if sudoku_map[row][col] == num:
                isYes = False
                break
    return isYes

def make_map(sudoku_map, zero_count):
    if zero_count == 0:
        for row in range(9):
            for col in range(9):
                print(sudoku_map[row][col], end=' ')
            print()
        exit()
    for row in range(9):
        for col in range(9):
            if sudoku_map[row][col] == 0:
                for num in range(1, 10):
                    if check_row(row, num) and check_col(col, num) and check_area(row,col,num):
                        sudoku_map[row][col] = num
                        make_map(sudoku_map, zero_count-1)
                        sudoku_map[row][col] = 0

make_map(sudoku_map, count_zero)

