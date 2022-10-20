# 오픈 채팅방 (Level 2)

from numpy import record


def solution(record):
    answer = [] # 결과 출력을 담은 변수
    members = dict() # 회원들의 아이디와 닉네임을 관리하기 위한 딕셔너리
    # 회원 정보를 관리할 반복분
    for i in record:
        cmd = i.split(' ') # record를 리스트로 만들기
        if cmd[0] == "Leave":
            continue
        members[cmd[1]] = cmd[2] # 항상 회원들의 정보를 최신 정보로 최신화
    
    # 명령어에 따른 결과를 리턴할 반복문
    for i in record:
        cmd = i.split(' ')
        if cmd[0] == "Enter":
            nickName = members[cmd[1]]
            temp = nickName+"님이 들어왔습니다."
        elif cmd[0] == "Leave":
            nickName = members[cmd[1]]
            temp =  nickName + "님이 나갔습니다."
        else:
            continue
        answer.append(temp)
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))