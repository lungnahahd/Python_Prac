# 방금 그 곡

def change_str(music): # 문자를 변환시켜서 코드의 간편함을 높힘
    music = music.replace('C#','c')
    music = music.replace('D#','d')
    music = music.replace('F#','f')
    music = music.replace('A#','a')
    music = music.replace('G#','g')
    return music


def solution(m, musicinfos):
    answer = ''
    result = ["(None)","-1","2400"] # 결과를 담을 배열 초기 세팅
    m = change_str(m)
    for i in musicinfos:
        music = i.split(",")
        music[3] = change_str(music[3])
        end = ''.join(music[1].split(":"))
        start = ''.join(music[0].split(":"))

        # 시간 처리 코드
        if end[:2] != start[:2]:
            if end[:2] == '00':
                end[0],end[1] = '2','4'
                end[:2] = '24'
            song_time = ((60 - int(start[2:])) + int(end[2:]) + 60*(int(end[:2]) - int(start[:2]) - 1))
        else:
            song_time = int(end) - int(start)
        check = ""
        # 시간에 맞게 멜로디를 나열
        for time in range(song_time):
            check += music[3][time%len(music[3])]
        if m in check:
            how_many = check.count(m)
            # 정답 도출 + 값이 동일하다면 빠르게 나온 악보가 정답..
            if (int(result[1]) < how_many) or (int(result[1]) == how_many and int(result[2]) > int(start)):
                result.clear()
                result.append(music[2])
                result.append(str(how_many))
                result.append(start)
    answer = result[0]


    return answer




print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC",["04:00,04:02,ZERO,ACC"]))