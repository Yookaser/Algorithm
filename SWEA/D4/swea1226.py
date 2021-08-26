# 1226. 미로1

# 방법1. bfs
def bfs(x, y):
    bfs_list = deque([(x, y)])
    visited = set([(x, y)])

    while bfs_list:
        x, y = bfs_list.popleft()

        if maze[x][y] == 3:  # 도착한 경우
            return 1

        for i in range(4):  # 상하좌우 반복
            nx, ny = x + dx[i], y + dy[i]  # 이동
            if (0 <= nx < 16) and (0 <= ny < 16):  # 범위 내인 경우
                if maze[nx][ny] != 1 and (nx, ny) not in visited:  # 벽이 아니고 방문한 적 없는 경우
                    bfs_list.append((nx, ny))  # 앞으로 방문할 곳 입력
                    visited.add((nx, ny))  # 방문 표시
    return 0  # 도착 못한 경우


from collections import deque

dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
for _ in range(10):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    print('#{} {}'.format(N, bfs(1, 1)))

# 방법2. dfs
def dfs(x, y):
    global result
    if maze[x][y] == 3:  # 도착한 경우
        result = 1  # 도착으로 표시
        return

    visited.add((x, y))

    for i in range(4):  # 상하좌우 반복
        nx, ny = x + dx[i], y+dy[i]  # 이동
        if (0 <= nx < 16) and (0 <= ny < 16):  # 범위 내인 경우
            if maze[nx][ny] != 1 and (nx, ny) not in visited:  # 벽이 아니고 방문한 적 없는 경우
                dfs(nx, ny)  # 재귀


dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
for _ in range(10):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = set()
    result = 0  # 기본값은 방문 못한 것으로

    dfs(1, 1)
    print('#{} {}'.format(N, result))