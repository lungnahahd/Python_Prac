# 암호만들기 (1759)
## 난이도 : 골드 5

mother_word = ['a','e','i','o','u']

cnt_pwd, cnt_word = list(map(int, input().split()))
word = list(input().split())
word.sort()

answer = []
temp = []
cnt_mother = 0

def bfs(start):
    global answer
    global temp
    global cnt_mother

    for idx in range(start, cnt_word):
        if word[idx] in mother_word:
            cnt_mother += 1
        temp.append(word[idx])
        if len(temp) == cnt_pwd:
            if cnt_mother >= 1 and cnt_pwd - cnt_mother >= 2:
                answer.append(''.join(temp))
        else:
            bfs(idx+1)
        if word[idx] in mother_word:
            cnt_mother -= 1
        temp.pop()
    
bfs(0)
for pwd in answer:
    print(pwd)