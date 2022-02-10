# 순서를 바꾸었을 때 같은 단어 그룹화하기
## n개의 단어가 입력으로 주어질 때, 한 단어에 속한 문자들의 순서를 바꾸어 만들 수 있는 단어들은 같은 그룹에 속한다고 정의된다고 합니다.
## 이 때 동일한 그룹에 속한 단어가 가장 많은 그룹의 단어 개수를 출력하는 코드를 작성해보세요.
# 입력은 1000 이므로 리스를 바로 정렬해도 무방!!!!

size = int(input())
countDic = dict()

for i in range(size):
    getWord = input()
    getWord = list(getWord)
    getWord.sort()
    editWord = "".join(getWord)
    if editWord in countDic:
        countDic[editWord] += 1
    else:
        countDic[editWord] = 1

valuesDic = countDic.values()
print(max(valuesDic))