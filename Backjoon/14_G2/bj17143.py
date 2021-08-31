# 17143. 낚시왕

import sys


def fishing(n):  # n번째 열에서 낚시
    for r in range(R):  # 행 반복
        if grf[r][n]:
            res = grf[r][n][2]
            grf[r][n] = 0  # 해당 좌표 초기화
            return res
    return 0  # 해당 열이 비어있었으면 0 반환(필수) 


def move():  # 상어 이동
    res = [[0] * C for _ in range(R)]  # 상어가 이동한 다음 맵이 될 공간

    for i in range(R*C):
        r, c = divmod(i, C)
        if grf[r][c]:  # 해당 좌표에 값이 있으면
            s, d ,z = grf[r][c]
            x = s  # 이동 횟수

            while x:
                nr, nc = r + dxy[d][0], c + dxy[d][1]
                if (-1<nr<R) and (-1<nc<C):  # 범위 안이면 진행
                    r, c = nr, nc
                    x -= 1
                else:  # 범위 밖이면 방향 변환
                    d = pair[d]

            if res[r][c]:  # 새 자표에 이미 값이 있으면 크기 비교 후 큰 것 저장
                if res[r][c][2] < z:
                    res[r][c] = (s, d, z)
            else:
                res[r][c] = (s, d, z)
    return res


input = sys.stdin.readline
R, C, M = map(int, input().split())
dxy = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]  # 상하우좌(0번 인덱스는 가짜)
grf = [[0] * C for _ in range(R)]  # 초기 맵
pair = {1: 2, 2: 1, 3: 4, 4: 3}  # 맞은편 좌표(위 <-> 아래, 오른쪽 <-> 왼쪽)

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if d in (1, 2):
        grf[r-1][c-1] = (s % ((R-1)*2), d, z)  # s(속도/이동거리)는 반복되므로 %를 한 값을 입력함
    else:
        grf[r-1][c-1] = (s % ((C-1)*2), d, z)  # s(속도/이동거리)는 반복되므로 %를 한 값을 입력함

ans = 0
for i in range(C):  # 열만큼 반복
    ans += fishing(i)
    grf = move()

print(ans)


## 더 좋은 move 함수 구현 ##
# def move():
#     res = [[0] * C for _ in range(R)]
#     for i in range(R):
#         for j in range(C):
#             if grf[i][j]:
#                 s, d, z = grf[i][j]
#                 x = i + dxy[d] * s
#                 y = j + dxy[d] * s
#                 while not (0 <= x < R):
#                     if x < 0:
#                         x = -x
#                         d = 3 - d
#                     if x >= R:
#                         x = 2 * (R - 1) - x
#                         d = 3 - d
#                 while not (0 <= y < C):
#                     if y < 0:
#                         y = -y
#                         d = 7 - d
#                     if y >= C:
#                         y = 2 * (C - 1) - y
#                         d = 7 - d
#                 if not res[x][y] or res[x][y][2] < z:
#                     res[x][y] = (s, d, z)
#     return res