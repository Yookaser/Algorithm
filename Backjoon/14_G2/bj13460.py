# 13460. 구슬 탈출 2

def move(x, y, dx, dy, c): # 벽 전이거나 'O'의 위치일 때까지 이동하는 함수(때문에 초기 빨간 구슬과 파란 구슬 있어도 상관 없음)
    while bead_map[x+dx][y+dy] != '#' and bead_map[x][y] != 'O':
        x += dx # dx, dy는 이동할 방향(상하좌우)
        y += dy
        c += 1 # 몇 칸 이동했는지(구슬이 겹치는 경우를 위해)
    return x, y, c


def bfs(s_rx, s_ry, s_bx, s_by):
    bfs_list = deque([(s_rx, s_ry, s_bx, s_by, 1)]) # 빨간 구슬 좌표, 파란 구슬 좌표, 반복 수
    visited.add((s_rx, s_ry, s_bx, s_by)) # 방문한 곳 표시

    while bfs_list:
        rx, ry, bx, by, cnt = bfs_list.popleft()
        if cnt > 10: # 반복을 10번 넘은 경우
            break
        
        for dx, dy in xy: # 상하좌우 이동할 좌표 반복
            drx, dry, rc = move(rx, ry, dx, dy, 0) # 빨간 구슬
            dbx, dby, bc = move(bx, by, dx, dy, 0) # 파란 구슬
            if bead_map[dbx][dby] == 'O': # 파란 구슬이 골인한 경우
                continue # 그냥 넘김
            if bead_map[drx][dry] == 'O': # 빨간 구슬이 골인한 경우(파란 구슬이 골인한 경우는 걸러짐)
                print(cnt)
                return
            if drx == dbx and dry == dby: # 빨간 구슬과 파란 구슬이 같은 경우
                if rc > bc: # 빨간 구슬이 더 많이 움직인 경우(즉, 파란 구슬보다 뒤에 있던 것)
                    drx -= dx # x, y 좌표 빼기
                    dry -= dy
                else:
                    dbx -= dx
                    dby -= dy
            if (drx, dry, dbx, dby) not in visited: # 방문한 적 없는 경우
                visited.add((drx, dry, dbx, dby))
                bfs_list.append((drx, dry, dbx, dby, cnt+1)) # 해당 좌표를 넣고 반복 +1
    print(-1) # 17line과 24 line을 동시에 처리하기 위해


import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
bead_map = [list(map(str, list(input().rstrip()))) for _ in range(N)]
visited = set() # 방문한 곳을 표시할 집합
xy = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 이동할 좌표

for i in range(N): # 초기 빨간 구슬과 파란 구슬의 좌표 찾기
    for j in range(M):
        if bead_map[i][j] == 'R':
            rx, ry = i, j
        elif bead_map[i][j] == 'B':
            bx, by = i, j

bfs(rx, ry, bx, by)