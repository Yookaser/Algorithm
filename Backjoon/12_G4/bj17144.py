# 17144. 미세먼지 안녕!(pypy3 제출)

import sys


def spread():
    temp = [[0] * C for _ in range(R)]  # 미세먼지를 옮길 새로운 2차원 리스트
    for i in range(R*C):
        r, c = divmod(i, C)
        if arr[r][c] == -1:  # 해당 좌표가 -1인 경우는 그냥 temp에 복사
            temp[r][c] = -1
            continue
        b = arr[r][c] // 5  # 확산될 값
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if (-1<nr<R) and (-1<nc<C) and arr[nr][nc] != -1:
                temp[nr][nc] += b  # 이동한 미세먼지 temp에 추가
                arr[r][c] -= b
        temp[r][c] += arr[r][c]  # 확산되고 남은 미세먼지 temp에 추가
    return temp


def cleaner():  # 바람 방향의 역방향으로 진행함
    ix, iy = air[0]  # 초기 좌표(상단 공기청소기)
    r, c = air[0][0] - 1, air[0][1]  # 미리 한 칸 이동시킴(아니면 공기청정기 자리 지워짐)
    for dr, dc in move:
        while True:
            nr, nc = r + dr, c + dc
            if (-1<nr<=ix) and (-1<nc<C) and (nr, nc) != (ix, iy):  # 범위 내(행의 범위는 초기 좌표까지), 이동 좌표가 초기 좌표가 아닌 경우
                arr[r][c] = arr[nr][nc]  # 이동
                r, c = nr, nc  # 좌표 갱신
            else:  # 위의 경우가 아닌 경우 지움
                break
    arr[r][c] = 0  # 공기청정기 바람이 처음 나오는 곳 0으로
            
    ix, iy = air[1]  # 초기 좌표(하단 공기청소기)
    r, c = air[1][0] + 1, air[1][1]
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:  # 이동 좌표를 새로 지정
        while True:
            nr, nc = r + dr, c + dc
            if (ix<=nr<R) and (-1<nc<C) and (nr, nc) != (ix, iy):
                arr[r][c] = arr[nr][nc]
                r, c = nr, nc
            else:
                break
    arr[r][c] = 0  # 공기청정기 바람이 처음 나오는 곳 0으로


input = sys.stdin.readline
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌
air = []

for i in range(R*C):  # 공기청소기 좌표 찾기
    r, c = divmod(i, C)
    if arr[r][c] == -1:
        air.append((r, c))

for _ in range(T):  # T(시간)만큼 반복
    arr = spread()
    cleaner()

ans = 0
for i in range(R*C):  # 남은 미세먼지 더해주기
    r, c = divmod(i, C)
    if arr[r][c] != -1:
        ans += arr[r][c]

print(ans)
