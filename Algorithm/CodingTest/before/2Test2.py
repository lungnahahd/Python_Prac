#2번 문제 : 풀이 중 반례 해결 못함
import heapq


def solution(arr,processes):
    answer = []
    writeTable = []
    readTable = []
    howlong = 0
    stateWrite = False
    for i in processes:
        temp = i.split()
        if len(timetable) == 0:
            print(...)



        else:
            if temp[0] == "write":
                heapq.heappush(timetable,("awrite",temp[1],temp[2],temp[3],temp[4],temp[5]))
            else:
                heapq.heappush(timetable,("read",temp[1],temp[2],temp[3],temp[4]))
            if not stateWrite:
                



        if howlong >= int(temp[1]) and stateWrite:
            if temp[0] == "write":
                heapq.heappush(timetable,("awrite",temp[1],temp[2],temp[3],temp[4],temp[5]))
            else:
                heapq.heappush(timetable,("read",temp[1],temp[2],temp[3],temp[4]))
        elif howlong >= int(temp[1]) and not stateWrite:
            if temp[0]









def solution(arr, processes):
    answer = []
    timetable = []
    timeLong = -1
    stateWrite = False
    for i in processes:
        #print(timetable)
        temp = i.split()
        if timeLong >= int(temp[1]) and stateWrite:
            if temp[0] == "write":
                heapq.heappush(timetable,("awrite",temp[1],temp[2],temp[3],temp[4],temp[5]))
            else:
                heapq.heappush(timetable,("read",temp[1],temp[2],temp[3],temp[4]))
        elif timeLong >= int(temp[1]) and not stateWrite:
            if temp[0] == "write":
                heapq.heappush(timetable,("awrite",temp[1],temp[2],temp[3],temp[4],temp[5]))
            else:
                timeLong = max(timeLong,int(temp[1])+int(temp[2]))
                get = arr[int(temp[3]):int(temp[4])+1]
                get = ''.join(get)
                answer.append(get)
        else:
            if len(timetable) == 0:
                nowList = temp
            else:

                if temp[0] == "read":
                    stateWrite = False
                    heapq.heappush(timetable,("read",temp[1],temp[2],temp[3],temp[4]))
                else:
                    stateWrite = True
                    heapq.heappush(timetable,("awrite",temp[1],temp[2],temp[3],temp[4],temp[5]))
                tempset = heapq.heappop(timetable)
                nowList = list(tempset)
            if nowList[0] == "read":
                stateWrite = False
                timeLong += int(nowList[2])
                get = arr[int(temp[3]):int(temp[4])+1]
                get = ''.join(get)
                answer.append(get)
            else:
                stateWrite = True
                timeLong += int(nowList[2])
                for j in range(int(nowList[3]),int(nowList[4]) + 1):
                    arr[j] = nowList[5]

    while len(timetable) != 0:
        tempset = heapq.heappop(timetable)
        nowList = list(tempset)
        if nowList[0] == "read":
            timeLong += int(nowList[2])
            get = arr[int(temp[3]):int(temp[4])+1]
            get = ''.join(get)
            answer.append(get)
        else:
            timeLong += int(nowList[2])
            for j in range(int(nowList[3]),int(nowList[4]) + 1):
                arr[j] = nowList[5]
    answer.append(timeLong)
    
    return answer




arr = ["1","2","4","3","3","4","1","5"]
#arr = ["1","1","1","1","1","1","1"]
processes = ["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]
#processes = ["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]
print(solution(arr,processes))
