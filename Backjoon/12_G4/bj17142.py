# 17142. 연구소 3

import sys
from collections import deque
from itertools import combinations


def bfs(p):
    res, cnt = 0, len(p)  # res => 최대 이동 값, cnt => 전파된 좌표의 개수
    v = [[-1] * N for _ in range(N)]  # -1 => 미방문, 이외의 수 => 시간
    q = deque()
    
    for r, c in p:  # 초기 q값 입력 & 초기값 0으로 방문 표시
        q.append((r, c))
        v[r][c] = 0
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if (-1<nr<N) and (-1<nc<N) and v[nr][nc] == -1 and G[nr][nc] != 1:
                cnt += 1
                v[nr][nc] = v[r][c] + 1
                q.append((nr, nc))
                
                if G[nr][nc] == 0:  # 0인 경우만 res를 갱신(이미 바이러스가 있는 경우는 전파가 아님)
                    res = max(res, v[nr][nc])

    if cnt == k:  # cnt와 k를 비교해서 같으면 res 반환, 아니면 전파 못하는 공간 있는 것이므로 2501 반환
        return res
    else:
        return 2501


input = sys.stdin.readline
N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

k = N**2  # 벽을 제외한 좌표의 개수를 의마할 것임
V = []  # 바이러스 좌표를 저장할 것임
for i in range(N**2):
    r, c = divmod(i, N)
    if G[r][c] == 2: V.append((r, c))
    elif G[r][c] == 1: k -= 1

ans = 2501  # 문제상 좌표의 개수가 2500개 이므로 +1하여 최대값 지정
P = list(combinations(V, M))  # dfs로 접근하면 시간초과 발생했음
for p in P:
    ans = min(ans, bfs(p))

if ans == 2501:
    print(-1)
else:
    print(ans)