# 1949. 등산로 조성

def dfs(x, y, h, c, d):  # x 좌표, y 좌표, 현재 높이, 카운팅, dig 가능 여부
    global ans
    v[x][y] = 1

    if c > ans:  # 종료 조건이 없으므로 매번 검사
        ans = c

    for dx, dy in xy:
        nx, ny = x + dx, y + dy
        if (-1<nx<N) and (-1<ny<N) and v[nx][ny] == 0:
            if h > arr[nx][ny]:  # 높이가 더 큰 경우
                dfs(nx, ny, arr[nx][ny], c + 1, d)  # 백트래킹
                v[nx][ny] = 0
            elif d and h > arr[nx][ny] - K:  # dig 가능하고, 그 높이도 가능한 경우
                dfs(nx, ny, h - 1, c + 1, False)  # 백트래킹
                v[nx][ny] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    m = 0
    for i in range(N**2):
        r, c = divmod(i, N)
        if arr[r][c] > m:
            m = arr[r][c]
    
    ans = 0
    xy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    s = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == m]

    for a, b in s:
        v = [[0] * N for _ in range(N)]  # 초기화는 매 좌표마다 해줘야 함
        dfs(a, b, m, 1, True)
    
    print(f'#{tc} {ans}')
