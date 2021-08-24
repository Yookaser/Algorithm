# 2638. 치즈

def bfs(x, y):
    dfs_list = deque([(x, y)])
    visited = set([(x, y)])  # 방문 표시

    while dfs_list:
        x, y = dfs_list.popleft()

        for dx, dy in move:
            nx, ny = x + dx, y + dy  # 이동
            if (0<=nx<N) and (0<=ny<M) and arr[nx][ny] != 3 and(nx, ny) not in visited:  # 범위내 / 3(근접했던 숫자) 아님 / 방문 X
                if arr[nx][ny] == 0:  # 다음 이동할 칸
                    dfs_list.append((nx, ny))
                    visited.add((nx, ny))
                elif arr[nx][ny] == 1:  # 치즈 근처인 경우
                    external.add((x, y))
                    arr[x][y] = 3


def cheeze(exter):
    result = []  # 반환 결과(녹아내릴 치즈 좌표)
    counting = {}  # 해당 좌표가 외부와 몇 칸을 맞대는지

    for x, y in exter:
        for dx, dy in move:
            nx, ny = x + dx, y + dy  # 이동
            if (0<=nx<N) and (0<=ny<M) and arr[nx][ny] == 1:  # 범위 내 / 해당 좌표가 치즈
                if counting.get((nx, ny)):  # 해당 좌표의 키가 있는 경우
                    counting[(nx, ny)] += 1
                else:
                    counting[(nx, ny)] = 1
    
    for key in counting:
        if counting[key] >= 2:  # 치즈와 인접 칸이 2칸 이상인 경우
            result.append(key)
            arr[key[0]][key[1]] = 0  # 해당 좌표 0으로

    return result  # 녹아 내릴 치즈 좌표 반환

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
external = set()  # 외부(치즈와 인접한 0) 좌표 저장(진행하다보면 외부가 아니게 되는데, 이걸 제거하는 코드를 추가하는 게 더 오래 걸림)
size, cnt = 0, 0  # 치즈 개수, 카운팅(결과)

for i in range(N*M):  # 치즈 개수 세기
    r, c = i // M, i % M  # row, col
    if arr[r][c] == 1:
        size += 1

bfs(0, 0)  # 외각 테두리는 0이 아니므로 임의의 점(0, 0)에서 시작

while size:
    temp = cheeze(external)  # 녹아내릴 치즈 반환 받음
    size -= len(temp)  # 해당 치즈 개수만큼 -
    for x, y in temp:  # 녹아내린 치즈 좌표에서 외부를 다시 확인(치즈 내부의 공간이 있을 수 있음)
        bfs(x, y)
    cnt += 1  # 카운팅

print(cnt)