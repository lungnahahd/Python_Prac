# 크기를 나타내는 N이 주어지고, 여행가의 이동 계획 내용이 제공
# 여행가가 최종적으로 도착할 지점의 좌표를 공백을 기준으로 구분하여 출력

import sys
input = sys.stdin.readline

move = input().strip()
move = int(move)

space_array = [[0] * move for _ in range(move)]
