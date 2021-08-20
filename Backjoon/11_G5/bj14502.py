# 14502. 연구소

def bfs(temp_map):
    global result, cut
    cnt = 0  # 새로 생성된 좀비의 수

    for row, col in zombie:  # 좀비가 있는 공간을 반복
        bfs_list = deque([(row, col)])

        while bfs_list:
            x, y = bfs_list.popleft()
            for dx, dy in move:
                nx = x + dx
                ny = y + dy
                if (0<=nx<N) and (0<=ny<M) and (temp_map[nx][ny]==0):  # 인덱스가 범위 내이고, 빈 공간인 경우(in blank를 안 쓴 것은 속도 때문)
                    cnt += 1
                    temp_map[nx][ny] = 2  # 좀비 칸으로 생성
                    bfs_list.append((nx, ny))

                    if cnt >= cut:  # 만약, 지금 최선의 결과보다 더 좋은 결과가 나올 수 없는 경우(시간 단축을 위함)
                        return

    if result < len(blank) - cnt - 3:  # 지금까지의 결과보다 더 좋은 경우
        cut = cnt  # 이 때의 cnt를 저장함(시간 단축을 위함)
        result = len(blank) - cnt - 3


def buildwall(depth, idx):  # 반복 수, 시작 인덱스
    if depth == 3:
        temp_map = deepcopy(research_map)  # bfs에서 내부 요소를 변경하므로 깊은 복사
        bfs(temp_map)
        return
    
    for i in range(idx, len(blank)):  # (시작 인덱스)~(빈 공간의 길이)
        research_map[blank[i][0]][blank[i][1]] = 1  # 해당 빈 공간에 벽을 세움
        buildwall(depth+1, i+1)  # 재귀(반드시 현재 인덱스의 +1로 해야 시간을 대폭 단축함)
        research_map[blank[i][0]][blank[i][1]] = 0  # 재귀 끝났으므로 벽을 내림


from copy import deepcopy
from collections import deque

N, M = map(int, input().split())
research_map = [list(map(int, input().split())) for _ in range(N)]
blank = [(i, j) for i in range(N) for j in range(M) if research_map[i][j] == 0]  # 빈 공간
zombie = [(i, j) for i in range(N) for j in range(M) if research_map[i][j] == 2]  # 좀비 공간

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상하좌우
result, cut = 0, len(blank)  # 결과값, 시간 단축을 위한 변수

buildwall(0, 0)
print(result)