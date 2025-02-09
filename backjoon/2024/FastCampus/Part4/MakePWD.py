# 암호만들기 (1759)
## 난이도 : 골드 5

mother_word = ['a','e','i','o','u'] # 모음 배열 (최소 1개 존재가 필요)

cnt_pwd, cnt_word = list(map(int, input().split()))
word = list(input().split())
word.sort()

answer = []
temp = []
cnt_mother = 0

def dfs(start):
    global answer
    global temp
    global cnt_mother # 모음 여부를 체크

    # 재귀 호출을 활용해서 백트래킹 진행
    for idx in range(start, cnt_word):
        if word[idx] in mother_word:
            cnt_mother += 1
        temp.append(word[idx])
        if len(temp) == cnt_pwd:
            if cnt_mother >= 1 and cnt_pwd - cnt_mother >= 2:
                answer.append(''.join(temp))
        else:
            dfs(idx+1)
        if word[idx] in mother_word:
            cnt_mother -= 1
        temp.pop()
    
dfs(0)
for pwd in answer:
    print(pwd)