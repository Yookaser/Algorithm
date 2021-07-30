# 2667. 단지번호붙이기

def bfs(x, y):
    bfs_list = [(x, y)] # 방문한 좌표를 저장
    visited_list = deque([(x, y)]) # bfs 순회를 위해 좌표 임시 저장
    cnt = 0 # 집의 개수를 카운팅

    while visited_list:
        x, y = visited_list.popleft()
        cnt += 1+
        for x_g, y_g in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]: # 위, 아래, 왼쪽, 오른쪽
            if complex[x_g][y_g] == 1 and (x_g, y_g) not in bfs_list: # 해당 좌표에 집이 있고, 방문한 적 없을 경우
                complex[x_g][y_g] = 0 # 카운팅했으므로 0으로 만들어줌
                bfs_list.append((x_g, y_g)) # 방문한 리스트 기록
                visited_list.append((x_g, y_g))

    return cnt # 사실 len(bfs_list)를 반환해도 될 것이라 예상

from collections import deque

N = int(input())
complex = [[0]*(N+2)] + [[] for _ in range(N)] + [[0]*(N+2)] # 인덱스를 편하게 받기 위해 가두리에 0을 추가함
result = []

for i in range(1, N+1):
    complex[i] = [0] + list(map(int, list(input()))) + [0] # 인덱스를 편하게 받기 위해 가두리에 0을 추가함

for x in range(1, N+1): # complex의 각 요소들을 순회하게 만듬(범위는 1~N까지 돌게해야 함)
    for y in range(1, N+1):
        if complex[x][y] == 1: # 해당 좌표에 집이 있는 경우(이미 카운팅됐거나 집이 없는 경우 0이므로)
            result.append(bfs(x, y)) # bfs에서 군집된 단지의 크기를 돌려 받음

result.sort()
print(len(result), *result, sep = '\n')