# 단어장
## n개의 단어(문자열)가 주어졌을 때, 각 단어가 몇 번씩 나왔는지를 앞선 단어가 먼저 나오도록 출력하는 프로그램을 작성해보세요.
### TreeSet 사용 이유 : 단어의 빈도수를 계속 정렬해야하고, 사전순 즉, 정렬해서 출력할 필요학 있으므로 사용

from sortedcontainers import SortedDict

note = SortedDict()      # treemap

size = int(input())

for i in range(size):
    word = input()
    if word in note:
        note[word] += 1
    else:
        note[word] = 1

for word,count in note.items():
    print(word,count)