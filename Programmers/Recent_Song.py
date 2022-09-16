# 방금 그 곡

def change_str(music):
    music = music.replace('C#','c')
    music = music.replace('D#','d')
    music = music.replace('F#','f')
    music = music.replace('A#','a')
    music = music.replace('G#','g')
    return music


def solution(m, musicinfos):
    answer = ''
    result = ["(None)","-1"]
    m = change_str(m)
    for i in musicinfos:
        music = i.split(",")
        music[3] = change_str(music[3])
        end = ''.join(music[1].split(":"))
        start = ''.join(music[0].split(":"))

        if end[:2] != start[:2]:
            song_time = ((60 - int(start[2:])) + int(end[2:]) + 60*(int(end[:2]) - int(start[:2]) - 1))
        else:
            song_time = int(end) - int(start)
        check = ""
        for time in range(song_time):
            check += music[3][time%len(music[3])]
        if m in check:
            how_many = check.count(m)
            if int(result[1]) < how_many:
                result.clear()
                result.append(music[2])
                result.append(str(how_many))
    answer = result[0]


    return answer




print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABCDEFG", ["11:50,12:04,HELLO,CDEFGAB", "12:57,13:11,BYE,CDEFGAB"]))