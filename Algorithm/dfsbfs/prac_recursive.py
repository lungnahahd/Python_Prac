def recursive_function(i):
    #재귀함수에는 반드시 종료 조건 필요
    if i == 10:
        return
    print(i, '번째 재귀 함수에서', i+1,'번째 재귀함수 호출')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료')


recursive_function(1)