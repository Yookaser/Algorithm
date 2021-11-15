# 2589. 보물섬

from sys import stdin
from collections import deque


def bfs(r, c):
    global ans
    q = deque([(r, c, 0)])
    vst[r][c] = 1
    f = -1  # 끝 노드 판별을 위한 변수(d가 f보다 작으면 추가 안되게)

    while q:
        r, c, d = q.popleft()
        flag = False  # 상하좌우가 다 막혔는지 판별할 변수

        for nr, nc in ((r-1, c), (r, c+1), (r+1, c), (r, c-1)):
            if (-1<nr<R) and (-1<nc<C) and grp[nr][nc] == 'L' and not vst[nr][nc]:
                flag = True  # 상하좌우가 안막혔으므로 True로
                vst[nr][nc] = 1  # 방문 표시
                q.append((nr, nc, d+1))
        
        if not flag and d > f:  # 끝노드 판별
            f = d  # 더 큰 수로 갱신
            end.append((r, c))  # 끝 노드 추가

    ans = max(ans, d)
    return r, c


input = stdin.readline
R, C = map(int, input().split())
grp = [list(input()) for _ in range(R)]

ans = 0
end = []  # 육지마다 끝노드(가장 먼 노드) 저장
vst = [[0] * C for _ in  range(R)]
for i in range(R*C):
    r, c = divmod(i, C)
    if not vst[r][c] and grp[r][c] == 'L':
        bfs(r, c)

for r, c in end[:]:  # end가 bfs 내부에서 append 되므로 [:]로 초기 end만 돌게 함
    vst = [[0] * C for _ in  range(R)]
    bfs(r, c)

print(ans)
