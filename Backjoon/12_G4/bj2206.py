<<<<<<< HEAD
# 2206. 벽 부수고 이동하기

def bfs(start_x, start_y, isbreak):
    bfs_list = deque([(start_x, start_y, isbreak)])
    visited[start_x][start_y][isbreak] = 1 # 첫 시작은 카운팅은 1(문제 조건)

    while bfs_list:
        x, y, isbreak = bfs_list.popleft()
        
        if x == (N-1) and y == (M-1): # 도착한 경우
            return visited[x][y][isbreak] # 해당 좌표의 값 반환(벽을 안부쉈다면 0번 인덱스 // 벽을 부쉈다면 1번 인덱스 값)
        
        for move in xy:
            next_x = x + move[0] # x좌표 이동값
            next_y = y + move[1] # y좌표 이동값

            if (0 <= next_x < N) and (0 <= next_y < M) and visited[next_x][next_y][isbreak] == 0: # x, y 좌표가 포함되어 있고, 해당 값을 방문한 적 없는 경우
                if node_map[next_x][next_y] == 1 and isbreak == 0: # 벽을 만났고, 벽을 한 번도 부수지 않았던 경우
                    bfs_list.append((next_x, next_y, 1)) # 벽을 부숴야 하므로 isbreak를 1로 입력
                    visited[next_x][next_y][1] = visited[x][y][isbreak] + 1 # isbreak는 1로하고, 카운팅 +1

                elif node_map[next_x][next_y] == 0: # 벽을 안만난 경우
                    bfs_list.append((next_x, next_y, isbreak)) # isbreak 값이 0이든 1이든 상관 없으므로 isbreak를 그냥 입력
                    visited[next_x][next_y][isbreak] = visited[x][y][isbreak] + 1 # 카운팅 +1
    return -1 # 답을 못 찾은 경우이므로 -1 반환


import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
xy = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 이동할 좌표(상우하좌)
visited = [[[0, 0] for _ in range(M)] for _ in range(N)] # 각 좌표의 인자는 [0, 0] // 0번 인덱스는 벽 안부순 상태의 카운팅, 1번은 벽 부순 상태의 카운팅
node_map = [list(map(int, list(input().rstrip()))) for _ in range(N)]

=======
# 2206. 벽 부수고 이동하기

def bfs(start_x, start_y, isbreak):
    bfs_list = deque([(start_x, start_y, isbreak)])
    visited[start_x][start_y][isbreak] = 1 # 첫 시작은 카운팅은 1(문제 조건)

    while bfs_list:
        x, y, isbreak = bfs_list.popleft()
        
        if x == (N-1) and y == (M-1): # 도착한 경우
            return visited[x][y][isbreak] # 해당 좌표의 값 반환(벽을 안부쉈다면 0번 인덱스 // 벽을 부쉈다면 1번 인덱스 값)
        
        for move in xy:
            next_x = x + move[0] # x좌표 이동값
            next_y = y + move[1] # y좌표 이동값

            if (0 <= next_x < N) and (0 <= next_y < M) and visited[next_x][next_y][isbreak] == 0: # x, y 좌표가 포함되어 있고, 해당 값을 방문한 적 없는 경우
                if node_map[next_x][next_y] == 1 and isbreak == 0: # 벽을 만났고, 벽을 한 번도 부수지 않았던 경우
                    bfs_list.append((next_x, next_y, 1)) # 벽을 부숴야 하므로 isbreak를 1로 입력
                    visited[next_x][next_y][1] = visited[x][y][isbreak] + 1 # isbreak는 1로하고, 카운팅 +1

                elif node_map[next_x][next_y] == 0: # 벽을 안만난 경우
                    bfs_list.append((next_x, next_y, isbreak)) # isbreak 값이 0이든 1이든 상관 없으므로 isbreak를 그냥 입력
                    visited[next_x][next_y][isbreak] = visited[x][y][isbreak] + 1 # 카운팅 +1
    return -1 # 답을 못 찾은 경우이므로 -1 반환


import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
xy = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 이동할 좌표(상우하좌)
visited = [[[0, 0] for _ in range(M)] for _ in range(N)] # 각 좌표의 인자는 [0, 0] // 0번 인덱스는 벽 안부순 상태의 카운팅, 1번은 벽 부순 상태의 카운팅
node_map = [list(map(int, list(input().rstrip()))) for _ in range(N)]

>>>>>>> a11fcf1c478ecacf60a3c5d41d3cc294e602f18d
print(bfs(0, 0, 0))