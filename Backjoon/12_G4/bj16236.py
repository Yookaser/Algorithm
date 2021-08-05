# 16236. 아기 상어

def bfs(x_init, y_init, size, cnt):
    is_find = False # 답을 찾았는지 여부
    result = [] # 결과들을 저장
    bfs_list = set([(x_init, y_init)]) # 중복 체크
    visited = deque([(x_init, y_init)])

    while visited:
        x, y = visited.popleft()
        for dx, dy in step:
            if sea_map[x+dx][y+dy] <= size and sea_map[x+dx][y+dy] != -1 and (x+dx, y+dy) not in bfs_list: # 사이즈보다 작거나 같고(이동 가능한지?) 테두리가 아니고 방문한 적 없는 경우
                if sea_map[x+dx][y+dy] != 0 and sea_map[x+dx][y+dy] < size: # 먹을 고기인 경우(조건을 나눠 준 것은 앞에 것이 False인 경우가 많은데 이 경우 조건문이 결정되므로 속도 향상될 것이라 생각)
                    is_find = True # 답을 찾았으므로 True 변환
                    bfs_list.add((x+dx, y+dy))
                    result.append((x+dx, y+dy, cnt+1)) # 결과들에 저장
                if is_find: # 만약 답을 찾았는데, 위의 if에서 안 걸린 경우 
                    bfs_list.add((x+dx, y+dy)) # 없어도 답은 맞음(다만, 중복으로 계산량을 줄일 수 있을 것이라 판단)
                    continue # bfs는 사방을 순서대로 진행하므로 답을 찾으면 더이상 visited에 추가하면 안됨
                else: # 답 못 찾았고, 먹을 고기가 아닌 경우
                    visited.append((x+dx, y+dy))
                    bfs_list.add((x+dx, y+dy))
        
        if x_init == x and y_init == y: # 깊이가 같은 경우(bfs는 상하좌우 방문 후, 해당 상하좌우의 상하좌우를 다시 방문하는데 이 깊이를 의미)
            cnt += 1 # 횟수 증가
            if visited: # 아직 방문할 곳이 남은 경우(깊이 카운트를 하기 위해)
                x_init = visited[-1][0] # 초기화
                y_init = visited[-1][1] # 초기화

    if not result: # 고기를 못 찾은 경우
        return 0, 0, 0
    elif len(result) == 1: # 먹을 고기가 1개인 경우(정렬의 시간을 아끼기 위해 분리함)
        sea_map[result[0][0]][result[0][1]] = 0 # 먹을 것이므로 해당 좌표값 0으로 바꿈
        return result[0]
    else:
        result.sort(key=lambda x: (x[2], x[0], x[1])) # 정렬(이때, 반드시 깊이(작은) -> 행(위쪽) -> 열(왼쪽)의 순서로 해야함 // 깊이가 다른 경우 있음 => 답을 깊이가 깊어지는 순간 바로 찾는 게 아님)
        sea_map[result[0][0]][result[0][1]] = 0 # 먹을 것이므로 해당 좌표값 0으로 바꿈
        return result[0]

from collections import deque

N = int(input())
sea_map = [[-1] * (N+2)] + [[] for _ in range(N)] + [[-1] * (N+2)] # 바다 구현(테두리 -1)

for i in range(1, N+1):
    sea_map[i] = [-1] + list(map(int,input().split())) + [-1] # sea_map 양식처럼 테두리 -1

for i in range(1, N+1): # 상어 첫 위치 찾기
    for j in range(1, N+1):
        if sea_map[i][j] == 9:
            x_state = i # x좌표
            y_state = j # y좌표
            sea_map[i][j] = 0 # 이동할 것이므로 해당값 0으로 바꿔줌
            break

cnt = 0 # 이동 횟수
eat = 0 # 먹은 횟수(성장하면 0으로 초기화 할 것)
size = 2 # 현재 크기
step = [(-1,0), (0,-1), (0,1), (1,0)] # 상좌우하(문제 요구사항이 있으므로 순서 중요함)

while 1: # 무한루프(True보다 1이 빠르다고 알고 있음)
    x, y, moves = bfs(x_state, y_state, size, 0) # bfs 실행(반환값은 2가지 => 먹을 고기를 찾은 경우, 못 찾은 경우)
    if  not moves: # 이동값이 없는 경우(더이상 먹을 고기가 없는 경우)
        break
    else: # 이동값이 있는 경우
        cnt += moves # 이동 수만큼 +
        x_state = x # x좌표를 받음
        y_state = y # y좌표를 받음
        eat += 1 # 해당 좌표 고기를 먹을 것이므로 +1
        if eat == size: # 먹은 수가 현재 크기와 같은 경우
            eat = 0 # 0으로 초기화
            size += 1 # 크기 +1

print(cnt)