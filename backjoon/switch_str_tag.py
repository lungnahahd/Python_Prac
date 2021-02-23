import sys
input = sys.stdin.readline

sentence = input().strip()
senlist= list(sentence)
count = len(senlist)
finallist = [0 for i in range(count)]
temp = [0 for i in range(count)]
wait = False
head = 0
if count == 1:
    print(sentence)
else:
    for i in range(count):
        if wait and senlist[i] != ">":
            finallist[i] = senlist[i]
            continue
        if senlist[i] == "<":
            wait = True
            finallist[i] = senlist[i]
            if head != 0:
                for j in range(head):
                    finallist[j] = temp[head - j] 
        elif senlist[i] == ">":
            wait = False
            finallist[i] = senlist[i]
        elif senlist[i] == " ":
            for j in range(head):
                finallist[j] = temp[head - j] 
        else:
            temp[head] = senlist[i]
            head += 1
print(finallist)
#print(''.join(finallist))







