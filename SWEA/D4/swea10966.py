# 10966. 물놀이를 가자

from collections import deque


def bfs():
    ans = 0
    q = deque()
    for i in range(N*M):
        r, c = divmod(i, M)
        if arr[r][c] == 'W':  # L이 아닌 W를 큐에 넣음(어차피 bfs는 동시에? 이동하므로)
            q.append((r, c))
            DP[r][c] = 0

    while q:
        x, y = q.popleft()
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if (-1<nx<N) and (-1<ny<M) and DP[nx][ny] == -1:  # 방문한 적 없는 경우
                DP[nx][ny] = DP[x][y] + 1  # 이동
                ans += DP[x][y] + 1  # 결과에 +
                q.append((nx, ny))
    return ans  # 결과 반환


T = int(input())
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    DP = [[-1] * M for _ in range(N)]

    print('#{0} {1}'.format(tc, bfs()))
