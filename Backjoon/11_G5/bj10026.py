# 10026. 적록색약

def bfs(x, y, color, bfs_list):
    bfs_list[x][y] = True # x, y를 방문하므로 True로
    visited_list = deque([(x, y)]) # 첫 방문이므로 deque로 선언

    while visited_list:
        x_s, y_s = visited_list.popleft() # 첫 번째 입력 좌표 반환

        for x_g, y_g in [(x_s-1, y_s), (x_s+1, y_s), (x_s, y_s-1), (x_s, y_s+1)]: # 상, 하, 좌, 우 이동
            if color_map[x_g][y_g] in color and not bfs_list[x_g][y_g]: # color_map이 입력받은 color에 포함되고, 방문한 적 없는 경우
                bfs_list[x_g][y_g] = True
                visited_list.append((x_g, y_g))

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

cnt_RG = 0 # 적록색약 카운팅
cnt_RGB = 0 # 정상 카운팅
color_map = [[0]*(N+2)] + [[] for _ in range(N)] + [[0]*(N+2)] # 맵 만들기(가두리 만드는 것)
bfs_list_RG = [[True] * (N+2)] + [[True] + [False] * N + [True] for _ in range(N)] + [[True] * (N+2)] # 적록색약의 방문 여부
bfs_list_RGB = [[True] * (N+2)] + [[True] + [False] * N + [True] for _ in range(N)] + [[True] * (N+2)] # 정상의 방문 여부

for i in range(1, N+1): # color_map 입력 받기
    color_map[i] = [0] + list(input()) + [0]

for i in range(1, N+1):
    for j in range(1, N+1):
        if not bfs_list_RGB[i][j]: # 방문한 적 없으면(정상)
            cnt_RGB += 1 # 카운팅 +1
            bfs(i, j, set(color_map[i][j]), bfs_list_RGB)

        if not bfs_list_RG[i][j]: # 방문한 적 없으면(적록색약)
            cnt_RG += 1 # 카운팅 +1
            if color_map[i][j] == 'B': # Black인 경우
                bfs(i, j, set(color_map[i][j]), bfs_list_RG)
            else: # Red, Green인 경우
                bfs(i, j, set(['R', 'G']), bfs_list_RG) # set(['R', 'G']) 만들기

print(cnt_RGB, cnt_RG)