# 15685. 드래곤 커브

def dragon_curve(x, y, g):
    if g == G:  # 입력받은 세대가 되면 종료
        return
    
    for idx in direction[len(direction)::-1]:  # 초기 입력된(for문 내부에서 추가된 건 제외) 방향의 역순으로 진행
        d = (idx+1) % 4  # 드래곤 커브는 이전 방향에서 +1한 뒤, 4로 나눈 나머지의 방향으로 진행함
        x += dx[d]
        y += dy[d]
        direction.append(d)  # 해당 방향 추가(다음 세대에서 이용해야 함)
        coords[x][y] = 1  # 해당 좌표 방문 표시

    dragon_curve(x, y, g+1)

import sys

input = sys.stdin.readline
N = int(input())
dx, dy = (0, -1, 0, 1), (1, 0, -1, 0)  # 우상좌하
coords = [[0] * 101 for _ in range(101)]  # 검사할 좌표(0으로 초기화)
result = 0  # 정사각형 개수

for _ in range(N):
    Y, X, D, G = map(int, input().split())

    direction = [D]  # 초기 드래곤 커브 0세대의 방향
    coords[X][Y], coords[X+dx[D]][Y+dy[D]] = 1, 1  # 초기 드래곤 커브 0세대의 좌표 방문 표시

    dragon_curve(X+dx[D], Y+dy[D], 0)  # 이동한 좌표 입력

for x in range(100):  # 범위는 0~99만 검사해야 함(문제 인덱스 조건)
    for y in range(100):
        if coords[x][y] and coords[x+1][y] and coords[x][y+1] and coords[x+1][y+1]:  # 네모 좌표가 모두 방문한 경우
            result += 1

print(result)