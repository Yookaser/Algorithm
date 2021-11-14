# 3055. 탈출

from sys import stdin
from collections import deque


input = stdin.readline
R, C = map(int, input().split())
grp = [list(input().rstrip()) for _ in range(R)]
vst = [[0] * C for _ in range(R)]
q = deque()

for i in range(R*C):
    r, c = divmod(i, C)
    if grp[r][c] == '*':  # 물 지역(방문 표시, q에 추가)
        vst[r][c] = 1
        q.append((r, c, 1))
    elif grp[r][c] == 'S':  # 시작 지역(방문 표시, 좌표 저장)
        vst[r][c] = 1
        sx, sy = r, c
    elif grp[r][c] == 'X':  # 벽 지역(방문 표시)
        vst[r][c] = 1

ans = 0
q.append((sx, sy, 0))  # 시작 지역을 반드시 제일 나중에 추가
while q and not ans:
    r, c, t = q.popleft()

    for nr, nc in ((r-1, c), (r, c+1), (r+1, c), (r, c-1)):
        if (-1<nr<R) and (-1<nc<C) and not vst[nr][nc]:
            if grp[nr][nc] == 'D':  # 도착한 경우
                if t: continue  # 물이 먼저 도착한 경우는 pass
                ans = vst[r][c]
                break
            vst[nr][nc] = vst[r][c] + 1
            q.append((nr, nc, t))

print(ans if ans else 'KAKTUS')  # 값에 따라 출력
