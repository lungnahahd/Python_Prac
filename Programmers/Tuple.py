# 튜플 (Level 2)

def solution(s):
    answer = []
    iSum = 0 # {}의 끝이나 시작 등을 처리할 수 있도록 해주는 변수(포인터 느낌..)
    save = set() # 중복 여부를 확인하기 위해 사용
    orderSave = dict() # 내부에 얼마나 있는지를 같이 적기 위해 사용
    for now in s[1:]: 
        if now == "{": # 배열의 시작
            iSum += 1
            tempSave = [] # 한 {} 안에 있는 수들을 담을 리스트
            countNum = 0 # 현재 리스트 내에 몇 개의 수가 있는지 카운트
            oneNum = "" # ,가 나오기 전까지 숫자를 이어 붙여서 두자리수 이상의 숫자를 잘 변환하기 위해 쓰는 변수
            continue
        elif now == "}": # 한 {}의 종료
            iSum -= 1 # 괄호가 닫혔음을 의미
            if iSum < 0: # 마지막 부분에서 낭비가 발생하지 않게 하기 위해 break
                break
            tempSave.append(int(oneNum)) # 숫자를 딕셔너리에 저장할 임시 리스트에 담기
            oneNum = ""
            temp = tempSave[:]
            orderSave[countNum] = temp # 임시 리스트의 크기를 key로 하고 임시 리스트를 value로 저장
        if iSum > 0 and now != ",": # 숫자인데 아직 한 숫자가 안 끝났을 수도 있으므로 바로 임시 배열에 넣지 말기 
            oneNum += now
        elif now == "," and iSum > 0: # {} 안에 ,일 경우만 들어가는 부분으로 한 숫자가 종료되었음을 의미
            nowNum = int(oneNum)
            oneNum = ""
            tempSave.append(nowNum)
            countNum += 1
    
    # 딕셔너리에서 순서대로 뺴서 최종 결과에 저장
    for idx in range(len(orderSave)):
        check = orderSave[idx]
        for cIdx in check: 
            if cIdx in save: # 중복 여부 확인 
                continue
            else:
                save.add(cIdx)
                answer.append(cIdx)
    return answer


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))
